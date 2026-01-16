import flet as ft
from core.routes import get_routes
from view.page.errors.page_404 import Error404Page
import warnings

# Silenciar warnings de Flet para mantener una terminal limpia y profesional
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

class DesktopRouter:
    """Router especializado para Desktop: Navegación directa."""
    
    @staticmethod
    def route_change(e):
        page = e if isinstance(e, ft.Page) else e.page
        routes = get_routes(page)
        
        # Gestión de Stack para Desktop (Permite botón 'Atrás')
        settings_route = "/settings" # Ejemplo de ruta modal
        
        # Si vamos al Home, limpiamos historial (Reinicio)
        if page.route == "/":
            page.views.clear()
        
        # Estrategia: Agregar siempre la vista actual al stack
        # Flet maneja la visualización de la última en la lista
        if page.route in routes:
            page.views.append(routes[page.route])
        else:
            page.views.append(Error404Page(page).get_view())
            
        page.update()

    @staticmethod
    def on_view_pop(view):
        page = view.page
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

    @staticmethod
    def navigate(page: ft.Page, route: str):
        """Navegación síncrona optimizada para Desktop."""
        page.go(route)
