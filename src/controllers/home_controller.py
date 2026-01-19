"""
Home Controller
===============
Controlador para la vista Home. Maneja la lógica de negocio.
"""
import flet as ft
from typing import Optional

from src.services.api_service import ApiService


class HomeController:
    """Controlador para la vista Home."""
    
    def __init__(
        self,
        page: ft.Page,
        view,
        api_service: ApiService
    ):
        """Inicializa el controlador."""
        self.page = page
        self.view = view
        self.api_service = api_service
    
    async def build(self) -> ft.View:
        """Construye y retorna la vista de Flet."""
        # Configurar eventos
        self.view.refresh_button.on_click = self.on_refresh_click
        self.view.create_button.on_click = self.on_create_click
        self.view.go_dashboard_button.on_click = self.on_dashboard_click
        
        # Construir ft.View
        return ft.View(
            route="/",
            controls=[
                self.view.build_content(),
            ],
            padding=0,
            bgcolor=ft.Colors.GREY_50,
        )
    
    async def initialize(self) -> None:
        """Inicializa los datos de la vista después de ser montada."""
        await self.load_items()
    
    async def load_items(self) -> None:
        """Carga los items desde la API."""
        try:
            self.view.loading.visible = True
            self.view.status_text.value = "Sincronizando..."
            self.page.update()
            
            items = await self.api_service.get_items()
            
            # Limpiar lista actual
            self.view.items_list.controls.clear()
            
            if items:
                # Mostrar solo los 5 más recientes en el panel lateral del Home
                for item in items[:5]:
                    self.view.items_list.controls.append(
                        self._create_item_card(item)
                    )
                self.view.status_text.value = f"{len(items)} productos en total"
            else:
                self.view.status_text.value = "Sin productos registrados"
            
        except Exception as e:
            self.view.status_text.value = f"Error de conexión"
        finally:
            self.view.loading.visible = False
            self.page.update()
    
    def _create_item_card(self, item: dict) -> ft.Container:
        """Crea una tarjeta minimalista para la lista de recientes."""
        is_available = item.get("is_available", False)
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(
                        ft.Icons.INVENTORY_2_OUTLINED,
                        color=ft.Colors.BLUE_700 if is_available else ft.Colors.RED_400,
                        size=20
                    ),
                    ft.Column(
                        controls=[
                            ft.Text(item.get("name", "N/A"), size=14, weight=ft.FontWeight.BOLD),
                            ft.Text(f"${item.get('price', 0):.2f}", size=12, color=ft.Colors.GREEN_700),
                        ],
                        spacing=0,
                        expand=True,
                    ),
                    ft.Icon(
                        ft.Icons.CHECK_CIRCLE if is_available else ft.Icons.CANCEL,
                        color=ft.Colors.GREEN_400 if is_available else ft.Colors.RED_400,
                        size=16
                    ),
                ],
            ),
            padding=15,
            bgcolor=ft.Colors.WHITE,
            border_radius=10,
            border=ft.border.all(1, ft.Colors.BLUE_50),
        )
    
    async def on_dashboard_click(self, e) -> None:
        """Navega a la vista de dashboard."""
        self.page.go("/dashboard")

    async def on_refresh_click(self, e) -> None:
        """Maneja el click en el botón de refrescar."""
        await self.load_items()
        
    async def on_create_click(self, e) -> None:
        """Maneja la creación de un nuevo producto."""
        name = self.view.name_input.value
        price_str = self.view.price_input.value
        description = self.view.desc_input.value
        is_available = self.view.available_check.value
        
        if not name:
            self.view.status_text.value = "Nombre obligatorio"
            self.page.update()
            return
            
        try:
            price = float(price_str) if price_str else 0.0
            
            # Crear item vía API
            item_data = {
                "name": name,
                "description": description,
                "price": price,
                "is_available": is_available
            }
            
            self.view.create_button.disabled = True
            self.view.loading.visible = True
            self.page.update()
            
            await self.api_service.create_item(item_data)
            
            # Limpiar y recargar
            self._clear_inputs()
            await self.load_items()
            self.view.status_text.value = f"'{name}' registrado"
            
        except ValueError:
            self.view.status_text.value = "Precio inválido"
        except Exception:
            self.view.status_text.value = "Error al guardar"
        finally:
            self.view.create_button.disabled = False
            self.view.loading.visible = False
            self.page.update()
            
    def _clear_inputs(self) -> None:
        """Limpia los campos del formulario."""
        self.view.name_input.value = ""
        self.view.price_input.value = ""
        self.view.desc_input.value = ""
        self.view.available_check.value = True
