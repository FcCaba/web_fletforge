import flet as ft

class ThemeColors:
    """
    Configuración de Identidad Visual Avanzada (Material 3).
    Define aquí todos los tokens de color para un control total del diseño.
    """
    # --- Colores de Marca ---
    PRIMARY = ft.Colors.CYAN_400
    ON_PRIMARY = ft.Colors.WHITE
    PRIMARY_CONTAINER = ft.Colors.BLUE_100
    ON_PRIMARY_CONTAINER = ft.Colors.BLUE_900

    SECONDARY = ft.Colors.BLUE_400
    ON_SECONDARY = ft.Colors.WHITE
    SECONDARY_CONTAINER = ft.Colors.BLUE_50
    ON_SECONDARY_CONTAINER = ft.Colors.BLUE_800

    TERTIARY = ft.Colors.AMBER_600
    ON_TERTIARY = ft.Colors.WHITE
    
    # --- Colores de Estado ---
    ERROR = ft.Colors.RED_600
    ON_ERROR = ft.Colors.WHITE
    SUCCESS = ft.Colors.GREEN_600
    WARNING = ft.Colors.ORANGE_600

    # --- Colores de Superficie (Adapta Blanco/Negro) ---
    SURFACE = ft.Colors.SURFACE
    ON_SURFACE = ft.Colors.ON_SURFACE # Negro en Light, Blanco en Dark
    
    # Fondos
    BACKGROUND = ft.Colors.SURFACE
    ON_BACKGROUND = ft.Colors.ON_SURFACE
    
    SURFACE_VARIANT = ft.Colors.SURFACE
    ON_SURFACE_VARIANT = ft.Colors.ON_SURFACE
    
    # Bordes
    OUTLINE = ft.Colors.OUTLINE
    OUTLINE_VARIANT = ft.Colors.OUTLINE

    
    # --- Colores Adicionales (Custom) ---
    # Aunque el Scheme de tu versión de Flet sea limitado,
    # puedes usar estas variables en tus componentes (Container, Text, etc.)
    TERTIARY = ft.Colors.AMBER_600
    ON_TERTIARY = ft.Colors.WHITE
    
    SURFACE_TINT = ft.Colors.BLUE_200
    INVERSE_SURFACE = ft.Colors.GREY_900
    INVERSE_PRIMARY = ft.Colors.CYAN_200
    
    SHADOW = ft.Colors.BLACK
    SCRIM = ft.Colors.BLACK

    # --- Colores de Componentes Específicos ---
    APPBAR_BG = PRIMARY
    APPBAR_TEXT = ON_PRIMARY
    
    FOOTER_BG = SURFACE
    FOOTER_TEXT = ON_SURFACE
    
    CARD_BG = SURFACE
    CARD_TEXT = ON_SURFACE

class ThemeStyles:
    """Tokens de Estilo Globales (Bordes, Sombras, etc.)"""
    BORDER_RADIUS = 12
    CARD_ELEVATION = 2
    CONTAINER_PADDING = 20

def get_app_theme():
    """
    Genera el tema PRINCIPAL de la aplicación (Cyan/Blue).
    """
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ThemeColors.PRIMARY,
            on_primary=ThemeColors.ON_PRIMARY,
            
            secondary=ThemeColors.SECONDARY,
            on_secondary=ThemeColors.ON_SECONDARY,
            
            surface=ThemeColors.SURFACE,
            on_surface=ThemeColors.ON_SURFACE,
            
            error=ThemeColors.ERROR,
            on_error=ThemeColors.ON_ERROR,
        )
    )

def get_alternative_theme():
    """
    Ejemplo de un SEGUNDO tema (Purple/Green).
    """
    return ft.Theme(
        color_scheme=ft.ColorScheme(
            # Ejemplo: Tema Morado
            primary=ft.Colors.PURPLE_500,
            on_primary=ft.Colors.WHITE,
            
            # Secundario Verde
            secondary=ft.Colors.LIME_500,
            on_secondary=ft.Colors.BLACK,
            
            # Superficie
            surface=ft.Colors.SURFACE,
            on_surface=ft.Colors.ON_SURFACE,
            
            error=ft.Colors.RED_700,
            on_error=ft.Colors.WHITE,
        )
    )
