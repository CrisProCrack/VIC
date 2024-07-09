import flet as ft
import ui_licenciatura
import componentes as cm
from flet_multi_page import subPage


class PanelUI(ft.Pagelet):

    def __init__(self):
        super().__init__()
        self.padding = 20
        self.appbar = cm.crear_app_bar(ft.icons.GRID_VIEW_SHARP, "UI (User Inteface)")
        
        #mkd_texto = ft.Markdown(
        #    cm.leer_archivo("assets/componentes.md"),
        #    selectable=True,
        #    extension_set="gitHubWeb",
        #    code_theme="atom-one-dark",
        #    code_style=ft.TextStyle(font_family="RobotoMono", size=16),
        #    on_tap_link=lambda e: self.page.launch_url(e.data),
        #)
        #mkd_texto = cm.crear_texto_markdown("assets/ui.md", self)

        btn_mostrar_ui = ft.FilledButton("Mostar UI",
                                         icon=ft.icons.ARROW_OUTWARD,
                                         width=200,
                                         on_click=lambda e: subPage(target=ui_licenciatura.main).start()
                         )
        
        #codigo  = cm.leer_archivo("ui_licenciatura.py")
        #mkd_codigo = ft.Markdown("```python\n" + codigo + "\n```",
        #                        selectable=True,
        #                        extension_set="gitHubWeb",
        #                        code_theme="atom-one-dark",
        #                        code_style=ft.TextStyle(font_family="RobotoMono", size=16)
        #                    )
        #codigo, mkd_codigo = cm.crear_codigo_markdown("ui_licenciatura.py")

        #txt_copiar = ft.Markdown("Código fuente para crear la UI.", selectable=True)
        #ico_copiar = ft.IconButton(ft.icons.COPY,
        #                    tooltip="Copiar código fuente",
        #                    on_click=lambda e: self.page.set_clipboard(codigo))
        #row_copiar = ft.Row([txt_copiar, ico_copiar])
        
        #self.content=ft.Row([ft.Column([mkd_texto, btn_mostrar_ui, row_copiar, mkd_codigo],
                                       #scroll=ft.ScrollMode.ALWAYS,
                                       #expand=True)])


if __name__ == "__main__":

    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window_height = 800
        page.padding = 0
        cnt_principal = ft.Container(content=PanelUI(), expand=True)
        page.add(cnt_principal)


    ft.app(target=main)
