import flet as ft


def crear_app_bar(icono, texto):
    ""
    return ft.AppBar(leading=ft.Icon(icono),
                     title=ft.Text(texto),
                     bgcolor=ft.colors.GREEN_200)


def leer_archivo(archivo):
    ""
    return open(archivo, 'r').read()


def crear_texto_markdown(archivo, pagelet):
    ""
    return ft.Markdown(
            leer_archivo(archivo),
            selectable=True,
            on_tap_link=lambda e: pagelet.page.launch_url(e.data)
        )


def crear_texto_markdown_formateado(archivo, pagelet):
    ""
    return ft.Markdown(
            leer_archivo(archivo),
            selectable=True,
            extension_set="gitHubWeb",
            code_theme="atom-one-dark",
            code_style=ft.TextStyle(font_family="RobotoMono", size=16),
            on_tap_link=lambda e: pagelet.page.launch_url(e.data)
        )


def crear_codigo_markdown(archivo):
    " Crea un componente Markdown y devuelve el contenido del archivo en texto plano"
    codigo  = leer_archivo(archivo)
    return codigo, ft.Markdown("```python\n" + codigo + "\n```",
                                selectable=True,
                                extension_set="gitHubWeb",
                                code_theme="atom-one-dark",
                                code_style=ft.TextStyle(font_family="RobotoMono", size=16)
                            )
