import flet as ft
from i18n.manager import i18n
from config.settings import Settings
from .base_layout import BaseLayout
from view.components.appbar_component import AppBarComponent
from view.components.footer_component import FooterComponent

class MainLayout(BaseLayout):
    """
    Componente de Layout Maestro.
    Integra AppBar, Footer y gestión de colores globales.
    """
    def __init__(self, page: ft.Page, title: str):
        super().__init__(page, title)

    def get_appbar(self, show_back: bool = False) -> ft.AppBar:
        """Retorna la barra de navegación usando el componente reutilizable."""
        return AppBarComponent(self.page, self.title, show_back=show_back)

    def get_footer(self) -> ft.Control:
        """Retorna el pie de página estándar."""
        return FooterComponent()

    def wrap_content(self, body: ft.Control) -> ft.Column:
        """
        Envuelve el contenido de la página en una estructura con Footer.
        Usa los colores definidos en Settings.
        """
        return ft.Column(
            [
                ft.Container(
                    content=body,
                    padding=20,
                    expand=True,
                    bgcolor=Settings.COLOR_BACKGROUND,
                    border_radius=ft.border_radius.only(top_left=20, top_right=20) if Settings.PLATFORM != "web" else 0
                ),
                self.get_footer()
            ],
            spacing=0,
            expand=True
        )

    def _change_language(self, lang: str):
        i18n.language = lang
        if self.page.on_route_change:
            self.page.on_route_change(self.page)
