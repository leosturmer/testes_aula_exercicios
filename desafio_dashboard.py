from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Input
from textual.containers import HorizontalGroup, VerticalGroup

from datetime import datetime


class Dashboard(App):
    CSS_PATH = 'desafio_dashboard.css'

    def compose(self) -> ComposeResult:

        with HorizontalGroup():
            yield Static(f'''

Este aqui é um texto! 
                         
Clicando nos botões, coisas acontecem!
                         
Digite um [u]número[/] ou [u]nome[/] 
              
''', id='st_principal')

            yield Static(f'\n\n\n\nAqui irá aparecer uma mensagem mágica...\n\n\n\n', id='st_segundo')

        with HorizontalGroup():
            yield Input(placeholder='Digite aqui...', id='input')

        with HorizontalGroup():

            yield Button('Nome...', variant='warning', id='bt_nome')

            yield Button('Número...', variant='error', id='bt_numero')

            yield Button('Horário...', variant='primary', id='bt_hora')

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == 'bt_nome':
            nome = self.query_one('#input', Input).value
            self.query_one('#st_segundo', Static).update(
                f'\n\n\n\n{nome}? Tem certeza disso?\nEu não gosto dessa pessoa...\n\n\n')

        if event.button.id == 'bt_numero':
            try:
                numero = int(self.query_one('#input', Input).value)
                numero2 = numero * 35

                self.query_one('#st_segundo', Static).update(
                    f'\n\n\n{numero} é seu número da sorte? \nEu prefiro {numero2}\n\n\n\n')

            except ValueError:
                self.query_one('#st_segundo', Static).update('Opa! Digite um número inteiro!')

        if event.button.id == 'bt_hora':
            dataehora = '%d/%m/%Y, %H:%M'
            dataagora = datetime.now().strftime(dataehora)

            self.query_one(f'#st_segundo', Static).update(f'\n\n\nData e hora: {dataagora}\nEstou te observando...\n\n\n\n')

        self.query_one('#input', Input).value = ''
        self.query_one('#input', Input).focus()


if __name__ == '__main__':
    app = Dashboard()
    app.run()
