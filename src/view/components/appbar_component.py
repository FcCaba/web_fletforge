import flet as ft
from config.theme import ThemeColors

class AppBarComponent(ft.AppBar):
    """
    Componente AppBar personalizado y reutilizable.
    """
    def __init__(self, page: ft.Page, title: str, show_back: bool = False):
        self._app_page = page
        
        leading = None
        if show_back:
            leading = ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color="onPrimary",
                on_click=lambda _: self._app_page.on_view_pop(self._app_page.views[-1])
            )

        super().__init__(
            title=ft.Text(
                title, 
                weight="bold", 
                color="onPrimary"
            ),
            bgcolor="primary",
            center_title=True,
            leading=leading,
            automatically_imply_leading=not show_back,
            actions=[
                ft.IconButton(
                    icon=ft.Icons.DARK_MODE if self._app_page.theme_mode == ft.ThemeMode.DARK else ft.Icons.LIGHT_MODE,
                    tooltip="Cambiar Tema",
                    icon_color="onPrimary",
                    on_click=self._toggle_theme
                ),
                ft.PopupMenuButton(
                    icon=ft.Icons.LANGUAGE,
                    icon_color="onPrimary",
                    items=[
                        ft.PopupMenuItem(
                            content=ft.Text("Español"),
                            on_click=self._create_change_language_handler("es")
                        ),
                        ft.PopupMenuItem(
                            content=ft.Text("English"),
                            on_click=self._create_change_language_handler("en")
                        ),
                    ]
                ),
                ft.Container(width=10)
            ]
        )

    async def _toggle_theme(self, e):
        """Cambia el tema y guarda la preferencia."""
        from services.persistence_service import PersistenceService
        
        is_dark = self._app_page.theme_mode == ft.ThemeMode.DARK
        new_mode = ft.ThemeMode.LIGHT if is_dark else ft.ThemeMode.DARK
        
        self._app_page.theme_mode = new_mode
        self._app_page.update()
        
        # Guardar persistencia
        storage = PersistenceService(self._app_page)
        await storage.set("theme_mode", "dark" if new_mode == ft.ThemeMode.DARK else "light")
        
        # Recargar para actualizar iconos (si es necesario) o simplemente cambiar icono
        if isinstance(e.control, ft.IconButton):
            e.control.icon = ft.Icons.DARK_MODE if new_mode == ft.ThemeMode.DARK else ft.Icons.LIGHT_MODE
            e.control.update()

    def _create_change_language_handler(self, lang: str):
        """Crea un manejador de eventos asíncrono para el cambio de idioma."""
        async def handler(e):
            await self._change_language(lang)
        return handler

    async def _change_language(self, lang: str):
        # Importación local para evitar circularidad
        from i18n.manager import i18n
        from services.persistence_service import PersistenceService
        
        # Cambiar y Guardar
        i18n.language = lang
        storage = PersistenceService(self._app_page)
        await storage.set("language", lang)
        
        # Propagar cambios
        if self._app_page.on_route_change:
            self._app_page.on_route_change(self._app_page)
