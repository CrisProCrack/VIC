from flet import *
from aplicacion import AplicacionView
from ayuda import AyudaView
from configuracion import ConfiguracionView
from usuario import UsuarioView

def main(page: Page):
    def route_change(route):
        page.views.clear()
        if page.route == "/" or page.route == "/aplicacion":
            page.views.append(
                View(
                    "/aplicacion",
                    [
                        AplicacionView(page)
                    ],
                )
            )
        elif page.route == "/ayuda":
            page.views.append(
                View(
                    "/ayuda",
                    [
                        AyudaView(page)
                    ],
                )
            )
        elif page.route == "/configuracion":
            page.views.append(
                View(
                    "/configuracion",
                    [
                        ConfiguracionView(page)
                    ],
                )
            )
        elif page.route == "/usuario":
            page.views.append(
                View(
                    "/usuario",
                    [
                        UsuarioView(page)
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    # Iniciar directamente en la vista de aplicación
    page.go("/aplicacion")

app(target=main)