import flet as ft
from config.theme import ThemeColors, ThemeStyles
from view.layout.main_layout import MainLayout
from i18n.manager import i18n

class HomePage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.layout = MainLayout(self.page, i18n.home_title)

    def get_view(self) -> ft.View:
        content = ft.Column(
            [
                ft.Container(
                    content=ft.Icon(ft.Icons.ROCKET_LAUNCH, size=100, color=ThemeColors.PRIMARY),
                    alignment=ft.Alignment(0, 0), # Fijado: Usando constructor explícito para evitar crash
                ),
                ft.Text(
                    i18n.welcome_message,
                    size=32,
                    weight="bold",
                    color=ThemeColors.ON_SURFACE,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    "Professional Architecture & Design System",
                    size=16,
                    color=ThemeColors.ON_SURFACE_VARIANT,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(height=30),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            i18n.go_to_details,
                            icon=ft.Icons.ARROW_FORWARD,
                            style=ft.ButtonStyle(
                                color=ThemeColors.ON_PRIMARY,
                                bgcolor=ThemeColors.PRIMARY,
                                shape=ft.RoundedRectangleBorder(radius=ThemeStyles.BORDER_RADIUS),
                            ),
                            on_click=lambda _: self.page.go("/details")
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )

        return ft.View(
            route="/",
            appbar=self.layout.get_appbar(),
            controls=[self.layout.wrap_content(content)],
            padding=0,
            bgcolor=ThemeColors.SURFACE,
        )
