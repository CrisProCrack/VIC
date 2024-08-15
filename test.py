import flet as ft

def main(page: ft.Page):
    page.title = "Interfaz de Aplicación"
    page.bgcolor = "#FFF0F5"  # Color de fondo rosa claro

    def create_card(text):
        return ft.Container(
            content=ft.Column([
                ft.Icon(ft.icons.SHAPE_LINE, size=40, color=ft.colors.GREY),
                ft.Icon(ft.icons.SQUARE, size=40, color=ft.colors.GREY),
                ft.Text(text, size=16, color=ft.colors.GREY),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
            width=150,
            height=150,
            bgcolor=ft.colors.WHITE,
            border_radius=10,
            padding=10,
        )

    sidebar = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        destinations=[
            ft.NavigationRailDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationRailDestination(icon=ft.icons.APPS, label="Aplicación"),
            ft.NavigationRailDestination(icon=ft.icons.BAR_CHART, label="Estadísticas"),
            ft.NavigationRailDestination(icon=ft.icons.HELP, label="Ayuda"),
            ft.NavigationRailDestination(icon=ft.icons.SETTINGS, label="Configuración"),
        ],
    )

    content = ft.Container(
        content=ft.Column([
            ft.Row([
                create_card("1st"),
                create_card("2nd"),
                create_card("3rd"),
                create_card("4th"),
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20),
            ft.Text(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                size=16,
                text_align=ft.TextAlign.CENTER,
                width=600,
            ),
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=30, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        expand=True,
        alignment=ft.alignment.center,
    )

    page.add(
        ft.Row([
            sidebar,
            ft.VerticalDivider(width=1),
            ft.Container(width=20),  # Espaciador
            content,
            ft.Container(width=20),  # Espaciador
        ], expand=True)
    )

ft.app(target=main)