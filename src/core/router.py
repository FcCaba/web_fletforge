"""
Async Router
============
Enrutador asíncrono para navegación entre vistas en Flet.
"""
import flet as ft
from typing import Callable, Dict, Any

from src.services.api_service import ApiService
from src.view.home_view import HomeView
from src.controllers.home_controller import HomeController
from src.view.dashboard_view import DashboardView
from src.controllers.dashboard_controller import DashboardController


class Router:
    """Enrutador asíncrono para la aplicación Flet."""
    
    def __init__(self, page: ft.Page):
        """Inicializa el router con la página de Flet."""
        self.page = page
        self.api_service = ApiService()
        
        # Registro de rutas: ruta -> (vista_class, controller_class)
        self.routes: Dict[str, tuple] = {
            "/": (HomeView, HomeController),
            "/dashboard": (DashboardView, DashboardController),
        }
    
    async def navigate(self, route: str) -> None:
        """Navega a la ruta especificada."""
        # Limpiar vistas anteriores
        self.page.views.clear()
        
        # Obtener la ruta base (sin parámetros)
        route_parts = route.split("/")
        base_route = "/" + "/".join(route_parts[1:2]) if len(route_parts) > 1 else "/"
        
        # Buscar la ruta en el registro
        if base_route in self.routes:
            view_class, controller_class = self.routes[base_route]
        else:
            # Ruta no encontrada, ir a home
            view_class, controller_class = self.routes["/"]
        
        # Crear instancias
        view = view_class()
        controller = controller_class(
            page=self.page,
            view=view,
            api_service=self.api_service
        )
        
        # Construir la vista
        flet_view = await controller.build()
        
        # Añadir vista a la pila
        self.page.views.append(flet_view)
        
        # Actualizar página
        self.page.update()
        
        # Inicializar controlador (carga de datos asíncrona)
        if hasattr(controller, "initialize"):
            await controller.initialize()
    
    def setup_listeners(self) -> None:
        """Configura los manejadores de eventos de la página."""
        self.page.on_route_change = self._on_route_change
        self.page.on_view_pop = self._on_view_pop
        print("⚡ [Router] Manejadores de eventos configurados")

    async def _on_route_change(self, e: ft.RouteChangeEvent) -> None:
        """Maneja los cambios de ruta disparados por la página."""
        print(f"⚡ [Router] Cambio de ruta detectado: {e.route}")
        await self.navigate(e.route)

    async def _on_view_pop(self, e: ft.ViewPopEvent) -> None:
        """Maneja el retroceso en la navegación."""
        if len(self.page.views) > 1:
            self.page.views.pop()
            top_view = self.page.views[-1]
            self.page.go(top_view.route)

    async def start(self) -> None:
        """Inicia el router navegando a la ruta actual."""
        initial_route = self.page.route or "/"
        print(f"⚡ [Router] Iniciando en ruta: {initial_route}")
        await self.navigate(initial_route)

    def register_route(self, route: str, view_class, controller_class) -> None:
        """Registra una nueva ruta en el router."""
        self.routes[route] = (view_class, controller_class)
