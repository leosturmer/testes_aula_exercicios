from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Input, Label, Header, Footer, TextArea

class UmaTela(App):
    
    TITLE = 'Brincando com CSS'
    SUB_TITLE = 'Testando o que fazer com o CSS por aqui'

    def compose(self) -> ComposeResult:
        yield Header(id='header')

        yield Static('''

Este é um programa para brincar com o uso do CSS!

''')

        yield Label ()

        yield Input(placeholder='Insira aqui o texto...')

        yield Button('Salvar texto', id='bt_cadastrar', classes='btn')
        yield Button('Limpar texto', id='bt_limpar', classes='btn')

        yield TextArea(disabled=True)

        yield Footer()


if __name__ == "__main__":
    app = UmaTela()
    app.run()