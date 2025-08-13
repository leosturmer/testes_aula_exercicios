from textual.app import App, ComposeResult
from textual.widgets import Static, Button, Input
from textual.containers import HorizontalGroup, VerticalGroup
from datetime import date, datetime, timedelta


class Dashboard(App):
    CSS_PATH = 'desafio_dashboard.css'

    formato_data = "%d/%m/%Y"

    dia_atual = datetime.today().date().strftime(formato_data)

    def compose(self) -> ComposeResult:
        
        with VerticalGroup():
            yield Static(f'Dia de hoje: {self.dia_atual} \n', id='nova_data')
            yield Input(placeholder='Some uma data...', id='data_soma')
            yield Button('Aperte aqui', variant='warning', id='bt_soma')

        with VerticalGroup():
            yield Static(f'Horário atual: {datetime.now().time()}')
            yield Button('Ou aqui!', variant='error', id='bt_error')

        with VerticalGroup():

            yield Static('3')
            yield Button('Não, aperta aqui', variant='primary', id='bt_primary')

        with VerticalGroup():

            yield Static('4')
            yield Button('É melhor apertar aqui...', variant='success', id='bt_sucess')


    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == 'bt_soma':
            data_somar = int(self.query_one('#data_soma', Input).value)
            nova_data = timedelta(days=data_somar)
            self.query_one('#nova_data', Static).update(f'Data com soma: {nova_data}')







if __name__ == '__main__':
    app = Dashboard()
    app.run()