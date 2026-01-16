import flet as ft
from config.theme import ThemeColors

class FooterComponent(ft.Container):
    """
    Componente Footer reutilizable para todas las páginas.
    """
    def __init__(self):
        super().__init__(
            content=ft.Column(
                [
                    ft.Divider(height=1, color=ThemeColors.OUTLINE_VARIANT),
                    ft.Row(
                        [
                            ft.Text(
                                "© 2024 FletForge",
                                size=12,
                                color=ThemeColors.ON_SURFACE_VARIANT,
                                weight="w500"
                            ),
                            ft.Row(
                                [
                                    ft.Icon(ft.Icons.AUTO_AWESOME, size=14, color=ThemeColors.PRIMARY),
                                    ft.Text("Powered by FletForge", size=12, italic=True, color=ThemeColors.ON_SURFACE_VARIANT),
                                ],
                                spacing=5
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ],
                spacing=10
            ),
            padding=ft.padding.only(top=20, bottom=10, left=20, right=20),
            bgcolor=ThemeColors.FOOTER_BG
        )
