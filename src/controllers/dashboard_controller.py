"""
Dashboard Controller
====================
Controlador para la vista de Dashboard. Maneja la lógica de visualización de datos.
"""
import flet as ft
from src.services.api_service import ApiService


class DashboardController:
    """Controlador para la vista Dashboard."""
    
    def __init__(self, page: ft.Page, view, api_service: ApiService):
        """Inicializa el controlador."""
        self.page = page
        self.view = view
        self.api_service = api_service
    
    async def build(self) -> ft.View:
        """Construye y retorna la vista de Dashboard."""
        self.view.back_button.on_click = self.on_back_click
        
        return ft.View(
            route="/dashboard",
            controls=[self.view.build_content()],
            padding=0,
            bgcolor=ft.Colors.GREY_50,
        )
    
    async def initialize(self) -> None:
        """Carga datos iniciales al entrar a la vista."""
        await self.load_data()
    
    async def load_data(self) -> None:
        """Carga y procesa los datos para el dashboard."""
        try:
            self.view.loading.visible = True
            self.page.update()
            
            items = await self.api_service.get_items()
            
            # Actualizar Estadísticas
            self.view.total_count.value = str(len(items))
            self.view.available_count.value = str(sum(1 for i in items if i.get("is_available")))
            
            # Actualizar Tabla
            self.view.data_table.rows.clear()
            for item in items:
                self.view.data_table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(item.get("id")))),
                            ft.DataCell(ft.Text(item.get("name", "N/A"), weight=ft.FontWeight.W_500)),
                            ft.DataCell(ft.Text(item.get("description", "N/A"), width=200)),
                            ft.DataCell(ft.Text(f"${item.get('price', 0):.2f}", color=ft.Colors.GREEN_700)),
                            ft.DataCell(
                                ft.Icon(
                                    ft.Icons.CHECK_CIRCLE if item.get("is_available") else ft.Icons.CANCEL,
                                    color=ft.Colors.GREEN_400 if item.get("is_available") else ft.Colors.RED_400
                                )
                            ),
                        ]
                    )
                )
        except Exception:
            pass
        finally:
            self.view.loading.visible = False
            self.page.update()
            
    async def on_back_click(self, e) -> None:
        """Vuelve a la vista principal."""
        self.page.go("/")
