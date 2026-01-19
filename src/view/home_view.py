"""
Home View
=========
Vista principal de la aplicación.
"""
import flet as ft


class HomeView:
    """Vista del Home con diseño moderno."""
    
    def __init__(self):
        """Inicializa los componentes de la vista."""
        # Estilos comunes
        self.primary_color = ft.Colors.BLUE_700
        
        # Header - Hero Section
        self.title = ft.Text(
            "Gestion De Productos",
            size=40,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.BLUE_900,
        )
        
        self.subtitle = ft.Text(
            "Gestión inteligente de inventario y productos",
            size=18,
            color=ft.Colors.BLUE_GREY_400,
        )
        
        # Dashboard Card
        self.go_dashboard_button = ft.ElevatedButton(
            content=ft.Text("Ir al Dashboard", size=16),
            icon=ft.Icons.DASHBOARD_ROUNDED,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_700,
                padding=20,
            ),
        )
        
        # --- Formulario de creación (Premium) ---
        self.name_input = ft.TextField(
            label="Nombre del Producto",
            tooltip=ft.Tooltip("Ej: MacBook Air M2"),
            border_radius=10,
            bgcolor=ft.Colors.BLUE_GREY_50,
            expand=True,
        )
        
        self.price_input = ft.TextField(
            label="Precio",
            tooltip=ft.Tooltip("0.00"),
            width=150,
            border_radius=10,
            bgcolor=ft.Colors.BLUE_GREY_50,
            keyboard_type=ft.KeyboardType.NUMBER,
            prefix="$ ",
        )
        
        self.desc_input = ft.TextField(
            label="Descripción Detallada",
            tooltip=ft.Tooltip("Características del producto..."),
            multiline=True,
            min_lines=1,
            max_lines=3,
            border_radius=10,
            bgcolor=ft.Colors.BLUE_GREY_50,
        )
        
        self.available_check = ft.Checkbox(
            label="Producto disponible para la venta",
            value=True,
            active_color=ft.Colors.GREEN_700,
        )
        
        self.create_button = ft.ElevatedButton(
            content=ft.Text("Registrar Producto", size=16, weight=ft.FontWeight.BOLD),
            icon=ft.Icons.SAVE_ALT_ROUNDED,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.GREEN_700,
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=25,
            ),
        )

        # Dashboard / Items Info
        self.status_text = ft.Text(
            "Listo",
            size=14,
            italic=True,
            color=ft.Colors.BLUE_GREY_300,
        )
        
        self.loading = ft.ProgressRing(width=20, height=20, stroke_width=2, visible=False)
        
        # Lista de items
        self.items_list = ft.Column(
            scroll=ft.ScrollMode.HIDDEN,
            spacing=15,
        )
        
        self.refresh_button = ft.IconButton(
            icon=ft.Icons.REFRESH_ROUNDED,
            tooltip=ft.Tooltip("Actualizar lista"),
            icon_color=ft.Colors.BLUE_700,
        )

    def build_content(self) -> ft.Control:
        """Construye el contenido principal de la vista."""
        return ft.Container(
            content=ft.Column(
                controls=[
                    # --- Header Section ---
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Column(
                                    controls=[self.title, self.subtitle],
                                    spacing=5,
                                    expand=True,
                                ),
                                self.go_dashboard_button,
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        padding=ft.padding.only(bottom=30),
                    ),
                    
                    ft.Row(
                        controls=[
                            # --- Left Panel: Creation ---
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Text("Añadir Nuevo Producto", size=22, weight=ft.FontWeight.W_600),
                                        ft.Divider(height=10, thickness=0),
                                        ft.Row([self.name_input, self.price_input], spacing=15),
                                        self.desc_input,
                                        ft.Row([self.available_check, self.create_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                                        ft.Row([self.loading, self.status_text], spacing=10),
                                    ],
                                    spacing=20,
                                ),
                                bgcolor=ft.Colors.WHITE,
                                padding=30,
                                border_radius=20,
                                shadow=ft.BoxShadow(blur_radius=20, color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)),
                                expand=2,
                            ),
                            
                            # --- Right Panel: Quick List ---
                            ft.Container(
                                content=ft.Column(
                                    controls=[
                                        ft.Row(
                                            [ft.Text("Recientes", size=22, weight=ft.FontWeight.W_600), self.refresh_button],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                        ),
                                        ft.Divider(height=10, thickness=0),
                                        ft.Container(
                                            content=self.items_list,
                                            expand=True,
                                        ),
                                    ],
                                    spacing=20,
                                ),
                                bgcolor=ft.Colors.BLUE_50,
                                padding=30,
                                border_radius=20,
                                expand=3,
                            ),
                        ],
                        spacing=30,
                        expand=True,
                    ),
                ],
                expand=True,
            ),
            padding=40,
            expand=True,
            bgcolor=ft.Colors.with_opacity(0.02, ft.Colors.BLUE_GREY_900),
        )
