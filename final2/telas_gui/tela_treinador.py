import PySimpleGUI as sg

class TelaTreinador:
    def __init__(self):
        layout=[
            [sg.Text('Dados Treinador')],
            [sg.Text('Nome'),sg.Input(size=20,key='nome')],
            [sg.Text('Idpokedex'),sg.Input(size=20,key='idpokedex')],
            [sg.Button('Continuar',key='continuar'), sg.Button('Voltar',key='voltar')]
        ]

        self.janela = sg.Window('Tela admin').Layout(layout)

    def abrir(self):
        while True:
            evento, valores=self.janela.Read()
            return evento, valores


class TelaTreinadorid:
    def __init__(self):
        layout=[
            [sg.Text('ID do Treinador que deseja selecionar')],
            [sg.Text('Idpokedex'), sg.Input(size=20, key='idpokedex')]
        ]

        self.janela = sg.Window('Tela admin').Layout(layout)

    def abrir(self):
        while True:
            evento, valores = self.janela.Read()
            return evento, valores