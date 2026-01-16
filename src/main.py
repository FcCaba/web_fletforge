import flet as ft
from config.settings import Settings
import warnings
import os

# Silenciar warnings de Flet globalmente para un inicio limpio en Windows
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

# Evitar ruidos de asyncio en Windows al cerrar la app
os.environ["PYTHONASYNCIODEBUG"] = "0"

def main(page: ft.Page):
    print(f"Iniciando proyecto FletForge ({Settings.PLATFORM})")
    
    try:
        # 1. Configuración de página
        Settings.configure_page(page)
        
        # 2. Persistencia y Configuración Dinámica
        from services.persistence_service import PersistenceService
        from i18n.manager import i18n
        
        storage = PersistenceService(page)
        
        # Cargar Tema
        saved_theme = storage.get("theme_mode", Settings.THEME_MODE)
        page.theme_mode = ft.ThemeMode.DARK if saved_theme == "dark" else ft.ThemeMode.LIGHT
        
        # Cargar Idioma
        saved_lang = storage.get("language", Settings.DEFAULT_LANGUAGE)
        i18n.language = saved_lang
        
        # 3. Selección de Router modular
        if Settings.PLATFORM == "mobile":
            from core.router_mobile import MobileRouter as AppRouter
        elif Settings.PLATFORM == "web":
            from core.router_web import WebRouter as AppRouter
        else:
            from core.router_desktop import DesktopRouter as AppRouter

        # 3. Vincular eventos (totalmente síncrono y profesional)
        page.on_route_change = AppRouter.route_change
        page.on_view_pop = AppRouter.on_view_pop
        page.on_back_button = AppRouter.on_view_pop
        
        # 4. Carga inicial sincronizada usando la ruta actual
        AppRouter.route_change(page)
        
    except Exception as e:
        print(f"Error fatal: {e}")
        page.add(ft.Text(f"Error fatal: {e}", color="red"))
        page.update()

if __name__ == "__main__":
    # Configuración dinámica para evitar errores en Mobile (Android/iOS)
    # El error 'TypeError: > not supported between NoneType and int' ocurre al pasar port=None
    run_args = {
        "main": main,
        "assets_dir": "assets",
        "view": Settings.get_app_view(),
    }
    
    if Settings.PLATFORM == "web":
        run_args["port"] = Settings.WEB_PORT
        run_args["web_renderer"] = Settings.WEB_RENDERER
        run_args["route_url_strategy"] = Settings.ROUTE_URL_STRATEGY

    try:
        ft.run(**run_args)
    except (ConnectionResetError, KeyboardInterrupt):
        # Silenciar errores de conexión al cerrar en Windows
        pass
