import flet as ft
import os
from .theme import ThemeColors, get_app_theme, get_alternative_theme

class Settings:
    APP_TITLE = "FletForge App"
    DEFAULT_LANGUAGE = "es"
    THEME_MODE = "light" # "light", "dark", "system"
    THEME_SELECTION = "alternative" # "default" o "alternative"
    DEFAULT_FONT_FAMILY = "MainFont"
    FONTS = {
        "MainFont": "fonts/BebasNeue-Regular.ttf",
    }
    
    # Configuración de Plataforma: "desktop", "web", "mobile"
    # Render inyecta la variable PLATFORM (si la configuras) o usa el default
    PLATFORM = os.environ.get("PLATFORM", "web")
    
    # Dimensiones fijas para móvil
    MOBILE_WIDTH = 390
    MOBILE_HEIGHT = 844

    # Configuración de Navegación
    # Render inyecta la variable PORT automáticamente
    WEB_PORT = int(os.environ.get("PORT", 8550))
    ROUTE_URL_STRATEGY = "path"

    # Mapeo de Colores para compatibilidad con Layouts
    COLOR_PRIMARY = ThemeColors.PRIMARY
    COLOR_ON_PRIMARY = ThemeColors.ON_PRIMARY
    COLOR_SECONDARY = ThemeColors.SECONDARY
    COLOR_SURFACE = ThemeColors.SURFACE
    COLOR_BACKGROUND = ThemeColors.BACKGROUND
    COLOR_ON_SURFACE = ThemeColors.ON_SURFACE
    
    # Nuevos Mapeos
    COLOR_ERROR = ThemeColors.ERROR
    COLOR_SUCCESS = ThemeColors.SUCCESS

    # Opciones de Renderizado Web
    WEB_RENDERER = "canvaskit"

    @staticmethod
    def configure_page(page: ft.Page):
        """Configura los parámetros de la página según la plataforma."""
        page.title = Settings.APP_TITLE
        page.theme_mode = Settings.THEME_MODE
        
        if Settings.FONTS:
            page.fonts = Settings.FONTS
        
        # Selección de Tema (Independiente de la fuente)
        # Puedes cambiar 'default' por 'alternative' para probar el otro tema
        if Settings.THEME_SELECTION == "alternative":
            page.theme = get_alternative_theme()
        else:
            page.theme = get_app_theme()
        
        if Settings.PLATFORM == "mobile":
            page.window.width = Settings.MOBILE_WIDTH
            page.window.height = Settings.MOBILE_HEIGHT
            page.window.resizable = False
            page.window.maximizable = False
            page.window.always_on_top = True
        elif Settings.PLATFORM == "desktop":
            page.window.resizable = True
            page.window.maximizable = True

    @staticmethod
    def get_app_view():
        """Retorna el modo de vista correcto para ft.app()."""
        if Settings.PLATFORM == "web":
            return ft.AppView.WEB_BROWSER
        return ft.AppView.FLET_APP
