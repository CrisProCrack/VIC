from flet import *
from aplicacion import AplicacionView, Conteo
from ayuda import AyudaView
from configuracion import ConfiguracionView
from usuario import UsuarioView
from imagenes import ImagenesView

def main(page: Page):
    def salir_aplicacion(page: Page):
        page.window_destroy()

    cnt_principal = Container(
        content=Text("Bienvenido"),
        expand=True
    )
    
    lst_pantallas = [
        Text("Inicio"),
        AplicacionView(page),  # Asumiendo que AplicacionView está definida y contiene Conteo
        ImagenesView(page),
        UsuarioView(page),
        Text("Estadísticas"),
        AyudaView(page),
        ConfiguracionView(page),
    ]
    
    def set_pantalla(e):
        if e.control.selected_index == 7:  # Índice de la opción "Salir"
            salir_aplicacion(page)
        else:
            if isinstance(cnt_principal.content, UserControl):
                cnt_principal.content.will_unmount()
            new_content = lst_pantallas[e.control.selected_index]
            cnt_principal.content = new_content
            
            if isinstance(new_content, UserControl):
                new_content.did_mount()
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
                label="Video en tiempo real"
            ),
            NavigationRailDestination(
                icon=icons.IMAGE_OUTLINED,
                selected_icon=icons.IMAGE,
                label="Imágenes"
            ),
            NavigationRailDestination(
                icon=icons.ACCOUNT_CIRCLE_SHARP,
                selected_icon=icons.ACCOUNT_CIRCLE,
                label="Usuarios"
            ),
            NavigationRailDestination(
                icon=icons.BAR_CHART_OUTLINED,
                selected_icon=icons.BAR_CHART,
                label="Estadísticas"
            ),
            NavigationRailDestination(
                icon=icons.HELP_OUTLINE,
                selected_icon=icons.HELP,
                label="Ayuda"
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon=icons.SETTINGS,
                label="Configuración"
            ),
            NavigationRailDestination(
                icon=icons.EXIT_TO_APP_SHARP,
                selected_icon=icons.EXIT_TO_APP,
                label="Salir"
            ),
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

if __name__ == "__main__":
    app(target=main)
