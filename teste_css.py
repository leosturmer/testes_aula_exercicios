from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Input, Header, Footer, TextArea
from textual.containers import HorizontalGroup

class UmaTela(App):

    CSS_PATH = 'teste_css.css'
    
    TITLE = 'Digite o seu texto'
    SUB_TITLE = 'E veja ele na área de visualização'

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)

        yield Static('''

Escreva um texto e clique em salvar.
O texto irá aparecer na área de visualização abaixo, uma linha por vez.
                     
''', id='static1')

        # yield Label (id='label1')

        with HorizontalGroup():
            yield Input(placeholder='Insira aqui o texto...', id='input1')

        with HorizontalGroup(id="container"):
        
            yield Button('Salvar texto', id='bt_salvar', classes='btn')
            yield Button('Limpar', id='bt_limpar', classes='btn')
            yield Button('Deletar texto', id='bt_deletar', classes='btn')           


        yield TextArea(read_only=True, show_cursor=False, id='textarea')

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == 'bt_limpar':
            for text in self.query('Input'):
                text.value = ''
            self.query_one('#input1').focus()

        if event.button.id == 'bt_deletar':
            self.query_one('#textarea', TextArea).text = ''
            self.query_one('#input1').focus()
            self.query_one('#input1', Input).value = ''


        if event.button.id == 'bt_salvar':
            if self.query_one('#input1', Input).value == '':
                self.query_one('#input1').focus()
                self.query_one('#input1', Input).value = ''
            else:
                texto_input = self.query_one('#input1', Input).value

                self.query_one('#textarea', TextArea).text += f'{texto_input} \n'
                self.query_one('#input1').focus()
                self.query_one('#input1', Input).value = ''



if __name__ == "__main__":
    app = UmaTela()
    app.run()