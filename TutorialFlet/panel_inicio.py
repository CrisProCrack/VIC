import flet as ft


class PanelInicio(ft.Pagelet):
    
    def __init__(self):
        super().__init__()
        img_ujat = ft.Image(src="img/dacyti.png", width=200, fit=ft.ImageFit.CONTAIN)
        txt_sistema = ft.Text("Tutorial de programación avanzada en Flet", size=30,
                              font_family="RobotoSlab", weight=ft.FontWeight.W_500,
                              color=ft.colors.GREEN_700)
        txt_version = ft.Text("Versión 1.0", size=20,
                              font_family="RobotoSlab", weight=ft.FontWeight.W_500,
                              color=ft.colors.GREEN_700)
        txt_info = ft.Text("Desarrollado con ❤️ por XYZ",
                           theme_style=ft.TextThemeStyle.BODY_LARGE)
        
        self.content=ft.Row([ft.Column([img_ujat, txt_sistema, txt_version, txt_info],
                                       alignment=ft.MainAxisAlignment.CENTER,
                                       horizontal_alignment=ft.CrossAxisAlignment.CENTER)],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER)


if __name__ == "__main__":

    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window_height = 800
        page.padding = 0
        cnt_principal = ft.Container(content=PanelInicio(), expand=True)
        page.add(cnt_principal)

    ft.app(target=main)
