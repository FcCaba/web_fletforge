"""
Dashboard View
==============
Vista de panel de control para visualización detallada de datos.
"""
import flet as ft


class DashboardView:
    """Vista del Dashboard con tabla de datos."""
    
    def __init__(self):
        """Inicializa los componentes de la vista."""
        # Botón volver
        self.back_button = ft.IconButton(
            icon=ft.Icons.ARROW_BACK_IOS_NEW_ROUNDED,
            tooltip=ft.Tooltip("Volver al Inicio"),
            icon_color=ft.Colors.BLUE_700,
        )
        
        # Estadísticas rápidas
        self.total_count = ft.Text("0", size=24, weight=ft.FontWeight.BOLD)
        self.available_count = ft.Text("0", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_700)
        
        # Tabla de datos
        self.data_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Producto")),
                ft.DataColumn(ft.Text("Descripción")),
                ft.DataColumn(ft.Text("Precio"), numeric=True),
                ft.DataColumn(ft.Text("Estado")),
            ],
            rows=[],
            heading_row_color=ft.Colors.BLUE_50,
            border=ft.border.all(1, ft.Colors.BLUE_GREY_50),
            border_radius=10,
        )
        
        self.loading = ft.ProgressBar(visible=False, color=ft.Colors.BLUE_700)

    def _create_stat_card(self, title: str, control: ft.Control, icon: str, color: str) -> ft.Container:
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(icon, color=color, size=30),
                    ft.Column(
                        controls=[
                            ft.Text(title, size=14, color=ft.Colors.BLUE_GREY_400),
                            control,
                        ],
                        spacing=0,
                    ),
                ],
                spacing=15,
            ),
            padding=20,
            bgcolor=ft.Colors.WHITE,
            border_radius=15,
            expand=True,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.with_opacity(0.05, ft.Colors.BLACK)),
        )

    def build_content(self) -> ft.Control:
        """Construye el contenido del dashboard."""
        return ft.Container(
            content=ft.Column(
                controls=[
                    # Header
                    ft.Row(
                        controls=[
                            ft.Row([self.back_button, ft.Text("Dashboard de Gestión", size=28, weight=ft.FontWeight.BOLD)]),
                            ft.Text("Gestion De Productos", size=14, color=ft.Colors.BLUE_GREY_300),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Divider(height=20, thickness=0),
                    
                    # Stats Row
                    ft.Row(
                        controls=[
                            self._create_stat_card("Total Productos", self.total_count, ft.Icons.INVENTORY_ROUNDED, ft.Colors.BLUE_400),
                            self._create_stat_card("En Stock", self.available_count, ft.Icons.CHECK_CIRCLE_ROUNDED, ft.Colors.GREEN_400),
                        ],
                        spacing=20,
                    ),
                    
                    ft.Divider(height=20, thickness=0),
                    
                    # Table Section
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row([ft.Text("Listado Detallado", size=20, weight=ft.FontWeight.W_600)]),
                                self.loading,
                                ft.Column([self.data_table], scroll=ft.ScrollMode.ALWAYS, expand=True),
                            ],
                            spacing=15,
                            expand=True,
                        ),
                        bgcolor=ft.Colors.WHITE,
                        padding=25,
                        border_radius=20,
                        expand=True,
                        shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.with_opacity(0.05, ft.Colors.BLACK)),
                    ),
                ],
                expand=True,
                spacing=0,
            ),
            padding=40,
            expand=True,
            bgcolor=ft.Colors.GREY_50,
        )
