import flet as ft
import componentes as cm
from flet_multi_page import subPage

class PanelConfiguracion(ft.Pagelet):

    def __init__(self):
        super().__init__()
        self.padding = 20
        self.appbar = cm.crear_app_bar(ft.icons.SETTINGS, "Configuración y puesta a punto")
        
        mkd_texto = cm.crear_texto_markdown_formateado("assets/config.md", self)
        #mkd_texto.on_tap_link=lambda e: self.page.launch_url(e.data)

        self.content=ft.Row([ft.Column([mkd_texto],
                                       scroll=ft.ScrollMode.ALWAYS,
                                       expand=True)])


if __name__ == "__main__":

    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window_height = 800
        page.padding = 0
        cnt_principal = ft.Container(content=PanelConfiguracion(), expand=True)
        page.add(cnt_principal)


    ft.app(target=main)
