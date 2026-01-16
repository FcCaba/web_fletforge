from view.page.view_home import HomePage
from view.page.view_details import DetailsPage
# Importar páginas aquí

def get_routes(page):
    """Diccionario centralizado de rutas del proyecto."""
    return {
        "/": HomePage(page).get_view(),
        "/details": DetailsPage(page).get_view(),
        # Agregar más rutas aquí
    }
