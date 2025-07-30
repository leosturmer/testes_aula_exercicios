from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Input
from textual.containers import HorizontalGroup, VerticalGroup

class Dashboard(App):
    CSS_PATH = 'desafio_dashboard.css'

    def compose(self) -> ComposeResult:
        
        with VerticalGroup():
            yield Static('1')
            yield Button('Aperte aqui', variant='warning', id='bt_soma')

        with VerticalGroup():
            yield Static('1')
            yield Button('Ou aqui!', variant='error', id='bt_error')

        with VerticalGroup():
            yield Static('3')
            yield Button('333333333', variant='primary')

 


    def on_button_pressed(self, event: Button.Pressed):
        pass



if __name__ == '__main__':
    app = Dashboard()
    app.run()