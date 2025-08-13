from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Input
from textual.containers import HorizontalGroup
from textual.color import Color

class Desafio(App):
    
    
    CSS = '''

Screen {
    padding-top: 3;
}

Static {
    height: 15;
    width: 15;
    margin-right: 1;
}

#st1 {
    background: rgb(0, 0, 0);
}

#st2 {
    background: rgb(0, 0, 0);
}

#st3 {
    background: rgb(0, 0, 0);
}

Button {
    margin-top: 1;
    align: center middle;
}

HorizontalGroup {
    align: center middle;
}

Input {
    width: 20;
    margin-top: 1;
}

Button {
    width: 20;
    margin-top: 1;
    margin-right: 1;
}

'''
    def __init__(self):
        super().__init__()
        self.cor1 = 0
        self.cor2 = 0
        self.cor3 = 0

    def compose(self):

        with HorizontalGroup():

            yield Static(id='st1')
            yield Static(id='st2')
            yield Static(id='st3')

        with HorizontalGroup():
            yield Input(placeholder='Valor RGB 1', id='input1')
            yield Input(placeholder='Valor RGB 2', id='input2')
            yield Input(placeholder='Valor RGB 3', id='input3')

        with HorizontalGroup():
            yield Button('Aperte aqui', id='bt_mudar')
            yield Button('Resetar', id='bt_resetar')

    
    def on_button_pressed(self, event: Button.Pressed):

        try:
            match event.button.id:
                case 'bt_mudar':

                    soma1 = int(self.query_one('#input1', Input).value)
                    soma2 = int(self.query_one('#input2', Input).value)
                    soma3 = int(self.query_one('#input3', Input).value)

                    self.cor1 += soma1
                    self.cor2 += soma2
                    self.cor3 += soma3
                    
                    st1 = self.query_one('#st1', Static)
                    st2 = self.query_one('#st2', Static)
                    st3 = self.query_one('#st3', Static)

                    st2.styles.background = Color(self.cor1, self.cor2, self.cor3)
                    st3.styles.background = Color(self.cor1, self.cor2, self.cor3)
                    st1.styles.background = Color(self.cor1, self.cor2, self.cor3)
                
                case 'bt_resetar':
                    st1 = self.query_one('#st1', Static)
                    st2 = self.query_one('#st2', Static)
                    st3 = self.query_one('#st3', Static)

                    st2.styles.background = Color(0, 0, 0)
                    st3.styles.background = Color(0, 0, 0)
                    st1.styles.background = Color(0, 0, 0)

        except ValueError:
            self.notify('Digite algum valor entre 0 e 255!')

if __name__ == '__main__':
    app = Desafio()
    app.run()