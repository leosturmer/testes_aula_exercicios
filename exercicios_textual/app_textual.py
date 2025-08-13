from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Input

class AppMinimo(App):

    CSS_PATH = "app_textual.css"

    nome = Input(placeholder='Digite seu nome...', id='tx_nome')

    def compose(self) -> ComposeResult:

        yield AppMinimo.nome

        yield Static('Uma mensagem!', id='msg1')
        yield Static('Outra mensagem!', id='msg2')

        yield Button('Me pressione', id='btn1')
        yield Button('Me pressione', id='btn2')

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == 'btn1':

            nome_exibicao = str(self.query_one("#tx_nome", Input).value)

            self.query_one('#msg1', Static).update('Mudei a mensagem!')
            self.query_one('#msg2', Static).update(f'Uma mensagem para {nome_exibicao}')

        if event.button.id == 'btn2':
            for static in self.query(Static):
                static.styles.background = 'aquamarine'

AppMinimo().run()