import flet as ft
from panel_inicio import PanelInicio
from panel_ui import PanelUI
from panel_configuracion import PanelConfiguracion


def main(page: ft.Page):
    """ Pantala principal """

    def set_pantalla(e: ft.ControlEvent):
        cnt_principal.content = lst_pantallas[e.control.selected_index]
        cnt_principal.update()

    # Configuración de la página
    page.fonts = {
        "RobotoMono": "RobotoMono-VariableFont_wght.ttf",
        "RobotoSlab": "RobotoSlab.ttf",
        "Caecilia":   "CaeciliaLTStd-Roman.otf"
    }
    page.title = 'Tutorial de programación avanzada en Flet'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_height = 850

    # Pantalla principal
    pnl_inicio = PanelInicio()
    cnt_principal = ft.Container(content=pnl_inicio, expand=True)
    
    lst_pantallas = [pnl_inicio, PanelConfiguracion(), PanelUI(), ft.Text("Pantalla 2"), ft.Text("Pantalla 3")]
    

    def set_pantalla(e):
        cnt_principal.content = lst_pantallas[e.control.selected_index]
        page.update()

    nav_rail = ft.NavigationRail(bgcolor=ft.colors.GREEN_200,
                                 selected_index=0,
                                 label_type=ft.NavigationRailLabelType.ALL,
                                 min_width=100,
                                 min_extended_width=400,
                                 group_alignment=-1,
                                 destinations=[ft.NavigationRailDestination(icon=ft.icons.HOME_OUTLINED,
                                                                           selected_icon=ft.icons.HOME,
                                                                           label="Inicio"),
                                               ft.NavigationRailDestination(icon=ft.icons.SETTINGS_OUTLINED,
                                                                           selected_icon=ft.icons.SETTINGS,
                                                                           label='Configuración'), 
                                               ft.NavigationRailDestination(icon=ft.icons.GRID_VIEW_OUTLINED,
                                                                           selected_icon=ft.icons.GRID_VIEW_SHARP,
                                                                           label="UI"),
                                               ft.NavigationRailDestination(icon=ft.icons.FOLDER_OUTLINED,
                                                                           selected_icon=ft.icons.FOLDER,
                                                                           label="Base de datos"),
                                               ft.NavigationRailDestination(icon=ft.icons.CLOUD_OUTLINED,
                                                                           selected_icon=ft.icons.CLOUD,
                                                                           label="En la nube"),
                                               ft.NavigationRailDestination(icon=ft.icons.HELP_OUTLINE,
                                                                           selected_icon=ft.icons.HELP,
                                                                           label="Ayuda")
                                               ],
                                 on_change=set_pantalla
                                )

    page.add(
        ft.Row([
                nav_rail,
                ft.VerticalDivider(width=1),
                ft.Column([cnt_principal], alignment=ft.MainAxisAlignment.START, expand=True),
               ],
               expand=True,
              )
            )


ft.app(target=main) # view=ft.AppView.WEB_BROWSER
# view=None
# web_renderer=ft.WebRenderer.HTML
