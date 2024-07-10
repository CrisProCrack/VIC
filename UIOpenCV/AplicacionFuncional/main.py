from flet import *
from aplicacion import AplicacionView
from ayuda import AyudaView
from configuracion import ConfiguracionView
from usuario import UsuarioView

def main(page: Page):
    def set_pantalla(e: ControlEvent):
        cnt_principal.content = lst_pantallas[e.control.selected_index]
        cnt_principal.update()

    pnl_inicio = AplicacionView(page)  # Proporcionar 'page' como argumento
    cnt_principal = Container(Text("WIP"), expand=True)
    #cnt_principal = Container(content=pnl_inicio, expand=True)
    
    lst_pantallas = [Text("WIP"), pnl_inicio, UsuarioView(page), ConfiguracionView(page), AyudaView(page)]
    
    def set_pantalla(e):
        cnt_principal.content = lst_pantallas[e.control.selected_index]
        page.update()
    
    nav_rail = NavigationRail(
        selected_index=0,
        label_type=NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=400,
        group_alignment=-1,
        destinations=[
            NavigationRailDestination(
                icon=icons.HOME_OUTLINED,
                selected_icon=icons.HOME,
                label="Inicio"
            ),
            NavigationRailDestination(
                icon=icons.LINKED_CAMERA_ROUNDED,
                selected_icon=icons.LINKED_CAMERA,
                label="Aplicación"
            ),
            NavigationRailDestination(
                icon=icons.ACCOUNT_CIRCLE_SHARP,
                selected_icon=icons.ACCOUNT_CIRCLE,
                label="Usuarios"
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon=icons.SETTINGS,
                label="Configuración"
            ),
            NavigationRailDestination(
                icon=icons.HELP_OUTLINE,
                selected_icon=icons.HELP,
                label="Ayuda"
            )
        ],
        on_change=set_pantalla
    )
    
    page.add(
        Row([
            nav_rail,
            VerticalDivider(width=1),
            cnt_principal
        ], expand=True)
    )
    
app(target=main)
