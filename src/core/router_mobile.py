import flet as ft
import time
from core.routes import get_routes
from view.page.errors.page_404 import Error404Page
from i18n.manager import i18n
import warnings

# Silenciar warnings de Flet para mantener una terminal limpia y profesional
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

class MobileRouter:
    """Router especializado para Móvil: Gestión de stack y botón atrás físico."""
    
    _last_back_press = 0
    
    @staticmethod
    def route_change(e):
        page = e if isinstance(e, ft.Page) else e.page
        routes = get_routes(page)
        
        page.views.clear()
        
        if "/" in routes:
            page.views.append(routes["/"])
            
        if page.route != "/" and page.route != "":
            if page.route in routes:
                page.views.append(routes[page.route])
            else:
                page.views.append(Error404Page(page).get_view())
        
        page.update()

    @staticmethod
    def on_view_pop(view):
        page = view.page
        
        # Si hay más de una vista, retrocedemos a la anterior
        if len(page.views) > 1:
            page.views.pop()
            top_view = page.views[-1]
            MobileRouter.navigate(page, top_view.route)
        
        # Si estamos en la base (Home), pedimos confirmación antes de salir
        elif page.route == "/" or page.route == "":
            now = time.time()
            if now - MobileRouter._last_back_press < 2:
                # El usuario confirmó la salida con doble toque
                page.window.destroy()
            else:
                MobileRouter._last_back_press = now
                snack = ft.SnackBar(ft.Text(i18n.exit_press_again), duration=2000)
                page.overlay.append(snack)
                snack.open = True
                page.update()
        
        # Si estamos en cualquier otra vista pero el stack está vacío (raro), volvemos a Home
        else:
            MobileRouter.navigate(page, "/")

    @staticmethod
    def navigate(page: ft.Page, route: str):
        """Navegación síncrona optimizada para Móvil."""
        page.go(route)
