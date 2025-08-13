from textual.app import App, ComposeResult
from textual.widgets import Button, Static

class ConsultaApp(App):
    def compose(self) -> ComposeResult:
        yield Static("Mensagem inicial", id="msg1")
        yield Static("Outra mensagem", id="msg2")
        yield Button("Atualizar todas", id="btn_all")
        yield Button("Atualizar uma", id="btn_one")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_all":
            # Atualiza todos os widgets Static
            for widget in self.query(Static):
                widget.update("Atualizado pelo botão 'Atualizar todas'!")
        elif event.button.id == "btn_one":
            # Atualiza apenas o widget com id 'msg1'
            widget = self.query_one("#msg1", Static)
            widget.update("Atualizado pelo botão 'Atualizar uma'!")