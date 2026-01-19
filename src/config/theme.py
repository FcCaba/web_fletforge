"""
Theme Configuration
===================
Configuración de temas y paleta de colores.
"""
import flet as ft


class Colors:
    """Paleta de colores de la aplicación."""
    
    # Primary Colors
    PRIMARY = ft.Colors.BLUE_700
    PRIMARY_LIGHT = ft.Colors.BLUE_400
    PRIMARY_DARK = ft.Colors.BLUE_900
    
    # Secondary Colors
    SECONDARY = ft.Colors.CYAN_600
    SECONDARY_LIGHT = ft.Colors.CYAN_400
    
    # Background Colors
    BACKGROUND = ft.Colors.GREY_100
    SURFACE = ft.Colors.WHITE
    
    # Text Colors
    TEXT_PRIMARY = ft.Colors.GREY_900
    TEXT_SECONDARY = ft.Colors.GREY_600
    
    # Status Colors
    SUCCESS = ft.Colors.GREEN_600
    WARNING = ft.Colors.ORANGE_600
    ERROR = ft.Colors.RED_600
    INFO = ft.Colors.BLUE_600


def apply_theme(page: ft.Page) -> None:
    """Aplica el tema personalizado a la página."""
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.theme = ft.Theme(
        color_scheme_seed=Colors.PRIMARY,
        color_scheme=ft.ColorScheme(
            primary=Colors.PRIMARY,
            secondary=Colors.SECONDARY,
            surface=Colors.SURFACE,
            error=Colors.ERROR,
        ),
    )
    
    page.dark_theme = ft.Theme(
        color_scheme_seed=Colors.PRIMARY,
        color_scheme=ft.ColorScheme(
            primary=Colors.PRIMARY_LIGHT,
            secondary=Colors.SECONDARY_LIGHT,
        ),
    )
