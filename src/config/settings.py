"""
App Settings
============
Configuración general de la aplicación.
"""
import os
import flet as ft
from dotenv import load_dotenv, find_dotenv

# Cargar variables de entorno buscando el archivo .env
env_file = find_dotenv()
if env_file:
    load_dotenv(env_file, override=True)
    print(f"🔧 Configuración cargada desde: {env_file}")
else:
    print("⚠️  No se encontró archivo .env, usando valores por defecto.")


class AppSettings:
    """Configuración general de la aplicación."""
    
    APP_NAME = "Gestion De Productos"
    VERSION = "0.1.0"
    
    # Platform Configuration
    # Options: "web", "desktop"
    # Se normaliza a minúsculas y se eliminan espacios
    PLATFORM = os.getenv("PLATFORM", "web").lower().strip()
    
    # Port configuration for deployment
    # Se intenta leer PORT (estándar en Render/Heroku/Docker)
    PORT = int(os.environ.get("PORT", os.getenv("PORT", "8550")))
    # Usamos 127.0.0.1 por defecto para que el navegador abra correctamente en local.
    # En producción (e.g. Render), la plataforma inyectará HOST=0.0.0.0
    HOST = os.environ.get("HOST", os.getenv("HOST", "127.0.0.1"))
    
    # API Settings
    API_TIMEOUT = 30  # seconds
    
    # UI Settings
    DEFAULT_PADDING = 16
    CARD_BORDER_RADIUS = 12
    BUTTON_BORDER_RADIUS = 8
    
    @classmethod
    def is_desktop(cls) -> bool:
        """Verifica si la aplicación está en modo escritorio."""
        return cls.PLATFORM == "desktop"
    
    @classmethod
    def is_web(cls) -> bool:
        """Verifica si la aplicación está en modo web."""
        return cls.PLATFORM == "web"
        
    @classmethod
    def configure_page(cls, page: ft.Page):
        """Configura los parámetros básicos de la página."""
        page.title = cls.APP_NAME
        page.padding = 0
        
        # Configuración de ventana para desktop
        if not page.web:
            page.window.width = 1000
            page.window.height = 800
            page.window.center()
    
    @classmethod
    def print_config(cls):
        """Imprime la configuración actual."""
        print(f"🔧 App Configuration:")
        print(f"   • Application: {cls.APP_NAME}")
        print(f"   • Platform:    {cls.PLATFORM.upper()}")
        print(f"   • Mode:        {'Desktop (Window + Server)' if cls.is_desktop() else 'Web (Server Only)'}")
