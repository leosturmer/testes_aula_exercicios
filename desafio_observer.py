from textual.app import App, ComposeResult
from textual.widgets import Static, Button
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
    background: rgb(37, 182, 182);
}

#st2 {
    background: rgb(37, 182, 182);
}

#st3 {
    background: rgb(37, 182, 182);
}

Button {
    margin-top: 1;
    align: center middle;
}

HorizontalGroup {
    align: center middle;
}

'''
    def __init__(self):
        super().__init__()
        self.cor1 = 37
        self.cor2 = 182
        self.cor3 = 182

    def compose(self):

        with HorizontalGroup():

            yield Static(id='st1')
            yield Static(id='st2')
            yield Static(id='st3')

        with HorizontalGroup():
            yield Button('Aperte aqui')

    
    def on_button_pressed(self, event: Button.Pressed):

        self.cor1 += 20
        self.cor2 -= 30
        self.cor3 += 40

        
        st1 = self.query_one('#st1', Static)
        st2 = self.query_one('#st2', Static)
        st3 = self.query_one('#st3', Static)

        st2.styles.background = Color(self.cor1, self.cor2, self.cor3)
        st3.styles.background = Color(self.cor1, self.cor2, self.cor3)
        st1.styles.background = Color(self.cor1, self.cor2, self.cor3)


if __name__ == '__main__':
    app = Desafio()
    app.run()