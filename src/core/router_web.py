import flet as ft
from core.routes import get_routes
from view.page.errors.page_404 import Error404Page
import warnings

# Silenciar warnings de Flet para mantener una terminal limpia y profesional
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

class WebRouter:
    """Router especializado para Web: Sincronización jerárquica con URLs limpias."""
    
    @staticmethod
    def route_change(e):
        page = e if isinstance(e, ft.Page) else e.page
        routes = get_routes(page)
        
        # Limpiamos para reconstruir el stack (estilo Breadcrumbs dinámico)
        page.views.clear()
        
        # 1. Siempre la base es el Inicio ("/")
        if "/" in routes:
            page.views.append(routes["/"])
        
        # 2. Análisis de segmentos por "/". Ejemplo: /detalles/categoria
        path_segments = [s for s in page.route.split("/") if s]
        accumulated_path = ""
        
        for segment in path_segments:
            accumulated_path += f"/{segment}"
            segment_key = f"/{segment}"
            
            # Prioridad 1: Coincidencia exacta de la ruta jerárquica (/detalles/categoria)
            if accumulated_path in routes and accumulated_path != "/":
                page.views.append(routes[accumulated_path])
            
            # Prioridad 2: El segmento existe como ruta raíz independiente (/categoria)
            elif segment_key in routes and segment_key != "/":
                page.views.append(routes[segment_key])
                
        # 3. Si no hay vistas (aparte del Home) y no estamos en el Home -> 404
        if len(page.views) == 1 and page.route != "/" and page.route != "":
             page.views.append(Error404Page(page).get_view())
             
        page.update()

    @staticmethod
    def on_view_pop(view):
        page = view.page
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            # En Web, si intentan "salir" del Home, simplemente recargamos o nos quedamos
            WebRouter.navigate(page, "/")

    @staticmethod
    def navigate(page: ft.Page, route: str):
        """Navegación síncrona optimizada para Web."""
        page.go(route)
