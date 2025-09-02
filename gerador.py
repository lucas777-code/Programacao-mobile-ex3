import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "Gerador de Senhas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 350
    page.window_height = 600
    page.padding = 20

    senha_atual = ""
    is_dark = False

    # ---------- Funções ----------
    def gerar_senha_customizada(e):
        nonlocal senha_atual
        comprimento = int(slider.value)
        caracteres = ""
        if upper_switch.value:
            caracteres += string.ascii_uppercase
        if lower_switch.value:
            caracteres += string.ascii_lowercase
        if numbers_switch.value:
            caracteres += string.digits
        if symbols_switch.value:
            caracteres += string.punctuation

        if caracteres:
            senha = "".join(random.choice(caracteres) for _ in range(comprimento))
            senha_output.value = senha
            senha_atual = senha
            copiar_btn.visible = True
        else:
            senha_output.value = "Selecione ao menos um tipo de caractere."
            senha_atual = ""
            copiar_btn.visible = False
        page.update()

    def gerar_senha_dificuldade(nivel):
        nonlocal senha_atual
        if nivel == "baixa":
            caracteres = string.ascii_lowercase
            comprimento = 6
        elif nivel == "media":
            caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits
            comprimento = 10
        elif nivel == "alta":
            caracteres = string.ascii_letters + string.digits + string.punctuation
            comprimento = 16

        senha = "".join(random.choice(caracteres) for _ in range(comprimento))
        senha_output.value = senha
        senha_atual = senha
        copiar_btn.visible = True
        page.update()

    def mostrar_senha_copiada(e):
        if senha_atual:
            text_display.value = f"Senha copiada: {senha_atual}"
            text_display.visible = True
            page.set_clipboard(senha_atual)
            page.update()

    def toggle_theme(e):
        nonlocal is_dark
        is_dark = not is_dark
        page.theme_mode = ft.ThemeMode.DARK if is_dark else ft.ThemeMode.LIGHT
        theme_button.icon = ft.Icons.DARK_MODE if is_dark else ft.Icons.LIGHT_MODE
        page.update()

    # ---------- Componentes ----------
    theme_button = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        on_click=toggle_theme
    )

    title_row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Gerador de Senhas", size=28, weight="bold"),
            theme_button
        ]
    )

    senha_output = ft.TextField(
        value="",
        label="Senha Gerada",
        read_only=True,
        width=280,
        text_align=ft.TextAlign.CENTER,
        bgcolor=ft.Colors.WHITE
    )

    text_display = ft.Text(
        value="",
        color=ft.Colors.GREEN,
        visible=False
    )

    copiar_btn = ft.ElevatedButton(
        text="COPIAR SENHA",
        on_click=mostrar_senha_copiada,
        color=ft.Colors.ON_SECONDARY,
        bgcolor=ft.Colors.SECONDARY,
        visible=False,
        width=180
    )

    slider = ft.Slider(
        min=8,
        max=20,
        value=12,
        divisions=12,
        label="CARACTERES: {value}"
    )

    upper_switch = ft.Switch(label="Letras maiúsculas")
    lower_switch = ft.Switch(label="Letras minúsculas", value=True)
    numbers_switch = ft.Switch(label="Incluir números")
    symbols_switch = ft.Switch(label="Incluir símbolos")

    preferencias_column = ft.Column(
        [
            ft.Text("PREFERÊNCIAS", size=16, weight="bold"),
            upper_switch,
            lower_switch,
            numbers_switch,
            symbols_switch
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    gerar_custom_btn = ft.ElevatedButton(
        text="PERSONALIZADA",
        on_click=gerar_senha_customizada,
        color=ft.Colors.ON_PRIMARY,
        bgcolor=ft.Colors.PRIMARY,
        width=140
    )

    gerar_baixa_btn = ft.ElevatedButton(
        text="FÁCIL",
        on_click=lambda e: gerar_senha_dificuldade("baixa"),
        color=ft.Colors.ON_PRIMARY,
        bgcolor=ft.Colors.BLUE,
        width=90
    )

    gerar_media_btn = ft.ElevatedButton(
        text="MÉDIA",
        on_click=lambda e: gerar_senha_dificuldade("media"),
        color=ft.Colors.ON_PRIMARY,
        bgcolor=ft.Colors.ORANGE,
        width=90
    )

    gerar_alta_btn = ft.ElevatedButton(
        text="DIFÍCIL",
        on_click=lambda e: gerar_senha_dificuldade("alta"),
        color=ft.Colors.ON_PRIMARY,
        bgcolor=ft.Colors.RED,
        width=90
    )

    # ---------- Layout ----------
    page.add(
        ft.Column(
            [
                title_row,
                senha_output,
                text_display,
                copiar_btn,
                slider,
                preferencias_column,
                gerar_custom_btn,
                ft.Row(
                    controls=[gerar_baixa_btn, gerar_media_btn, gerar_alta_btn],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
    )

ft.app(
    target=main,
    assets_dir="assets"
)