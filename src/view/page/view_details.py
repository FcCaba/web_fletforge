import flet as ft
from config.theme import ThemeColors, ThemeStyles
from view.layout.main_layout import MainLayout
from i18n.manager import i18n

class DetailsPage:
    def __init__(self, page: ft.Page):
        self.page = page
        self.layout = MainLayout(self.page, i18n.details_title)

    def get_view(self) -> ft.View:
        content = ft.Column(
            [
                ft.Container(
                    content=ft.Icon(ft.Icons.INFO_OUTLINE, size=80, color=ThemeColors.SECONDARY),
                    alignment=ft.Alignment(0, 0), # Fijado: Usando constructor explícito
                ),
                ft.Text(
                    i18n.details_content, 
                    size=24, 
                    weight="bold", 
                    color=ThemeColors.ON_SURFACE,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Container(height=20),
                ft.Row(
                    [
                        ft.OutlinedButton(
                            i18n.back_to_home,
                            icon=ft.Icons.ARROW_BACK,
                            style=ft.ButtonStyle(
                                color=ThemeColors.PRIMARY,
                                shape=ft.RoundedRectangleBorder(radius=ThemeStyles.BORDER_RADIUS),
                            ),
                            on_click=lambda _: self.page.go("/")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True
        )
        
        return ft.View(
            route="/details",
            appbar=self.layout.get_appbar(show_back=True),
            controls=[self.layout.wrap_content(content)],
            padding=0,
            bgcolor=ThemeColors.SURFACE,
        )
