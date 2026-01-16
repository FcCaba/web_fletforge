import flet as ft
from abc import ABC, abstractmethod

class BaseLayout(ABC):
    """
    Interface base para todos los Layouts en FletForge.
    Asegura consistencia en AppBar, Footer y estructura de contenido.
    """
    def __init__(self, page: ft.Page, title: str):
        self.page = page
        self.title = title

    @abstractmethod
    def get_appbar(self, show_back: bool = False) -> ft.AppBar:
        """Debe retornar el objeto AppBar configurado."""
        pass

    @abstractmethod
    def get_footer(self) -> ft.Control:
        """Debe retornar el objeto Footer (pie de página)."""
        pass

    @abstractmethod
    def wrap_content(self, body: ft.Control) -> ft.Control:
        """Debe envolver el contenido principal en un contenedor o estructura."""
        pass
