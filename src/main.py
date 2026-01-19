"""
Flet Application Entry Point
============================
Punto de entrada principal de la aplicación Flet.
"""
import os
import sys
import threading
import time
import uvicorn
import flet as ft

# Asegurar que el directorio raíz esté en el path para las importaciones
# Esto permite que 'from backend...' funcione desde 'src/main.py'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.core.router import Router
from src.config.theme import apply_theme
from src.config.settings import AppSettings


def run_backend():
    """Ejecuta el servidor FastAPI backend."""
    try:
        from backend.main import app as fastapi_app
        print("🚀 [Backend] Iniciando en http://127.0.0.1:8000")
        uvicorn.run(fastapi_app, host="127.0.0.1", port=8000, log_level="error")
    except Exception as e:
        print(f"❌ [Backend] Error: {e}")


async def main(page: ft.Page):
    """Función principal de la aplicación Flet."""
    print(f"⚡ [Flet] Iniciando main. Modo: {'WEB' if page.web else 'DESKTOP'}")
    
    # 1. Configuración Básica (desde Settings)
    AppSettings.configure_page(page)
    
    # 2. Aplicar Tema
    apply_theme(page)
    
    # 3. Inicializar Router y Eventos
    router = Router(page)
    router.setup_listeners()
    
    # 4. Iniciar Navegación
    await router.start()


# Orquestación de Backend y Lanzamiento
def start_app():
    # Iniciar Backend en hilo separado
    threading.Thread(target=run_backend, daemon=True).start()
    time.sleep(1)
    
    # Lanzar Flet
    if AppSettings.is_web():
        ft.run(
            main,
            host=AppSettings.HOST,
            port=AppSettings.PORT,
            view=ft.AppView.WEB_BROWSER,
            web_renderer=ft.WebRenderer.CANVAS_KIT
        )
    else:
        ft.app(target=main)


if __name__ == "__main__":
    start_app()
