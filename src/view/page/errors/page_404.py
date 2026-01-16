import flet as ft
from config.theme import ThemeColors, ThemeStyles
from view.layout.main_layout import MainLayout
from i18n.manager import i18n

class Error404Page:
    def __init__(self, page: ft.Page):
        self.page = page
        self.layout = MainLayout(self.page, "404 Not Found")

    def get_view(self) -> ft.View:
        content = ft.Column(
            [
                ft.Container(
                    content=ft.Icon(ft.Icons.ERROR_OUTLINE, size=100, color=ThemeColors.ERROR),
                    alignment=ft.Alignment(0, 0), # Fijado: Usando constructor explícito
                ),
                ft.Text("404", size=60, weight="bold", color=ThemeColors.ERROR),
                ft.Text(i18n.page_not_found, size=20, color=ThemeColors.ON_SURFACE),
                ft.Container(height=30),
                ft.FilledButton(
                    i18n.back_to_home,
                    icon=ft.Icons.ARROW_BACK,
                    style=ft.ButtonStyle(
                        bgcolor=ThemeColors.PRIMARY, 
                        color=ThemeColors.ON_PRIMARY,
                        shape=ft.RoundedRectangleBorder(radius=ThemeStyles.BORDER_RADIUS),
                    ),
                    on_click=lambda _: self.page.go("/")
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )

        return ft.View(
            route="/404",
            appbar=self.layout.get_appbar(show_back=True),
            controls=[self.layout.wrap_content(content)],
            padding=0,
            bgcolor=ThemeColors.SURFACE,
        )
