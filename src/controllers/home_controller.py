import flet as ft

class HomeController:
    def __init__(self, model, page: ft.Page):
        self.model = model
        self.page = page

    def handle_start(self):
        """Maneja el evento de inicio del usuario de forma síncrona y profesional."""
        print("Navegando a detalles...")
        
        # Usamos go() para sincronizar la barra de direcciones (Warnings silenciados en el core)
        self.page.go("/details")
