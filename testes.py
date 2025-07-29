from textual.app import App, ComposeResult
from textual.widgets import Button, Static

class ContadorApp(App):
    def __init__(self):
        super().__init__()
        self.contador = 0

    def compose(self) -> ComposeResult:
        yield Button("Incrementar", id="inc")
        yield Static(f"Valor: {self.contador}", id="valor")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.contador += 1
        self.query_one("#valor", Static).update(f"Valor: {self.contador}")

ContadorApp().run()