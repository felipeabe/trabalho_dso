import PySimpleGUI as sg

class TelaDadosPokemon:
    def __init__(self):
        sg.ChangeLookAndFeel('DarkGreen1')
        layout=[
            [sg.Text('Nome',size=16),sg.Input(size=20,key='nome')],
            [sg.Text('Tipo',size=16),sg.Input(size=20,key='tipo')],
            [sg.Text('Level',size=16), sg.Input(size=20, key='level')],
            [sg.Text('Nome do ataque 1',size=16), sg.Input(size=20, key='nomeataque1')],
            [sg.Text('Valor do ataque 1',size=16), sg.Input(size=20, key='valorataque1')],
            [sg.Text('Nome do ataque 2',size=16), sg.Input(size=20, key='nomedoataque2')],
            [sg.Text('Valor do ataque 2',size=16), sg.Input(size=20, key='valorataque2')],
            [sg.Text('Defesa',size=16), sg.Input(size=20, key='defesa')],
            [sg.Text('Região',size=16), sg.Input(size=20, key='regiao')],
            [sg.Button('OK',key='ok'), sg.Button('Cancelar',key='cancelar')]
        ]

        self.janela = sg.Window('Dados Pokemon').Layout(layout)

    def abrir(self):
        while True:
            evento, valores=self.janela.Read()
            return evento, valores


class TelaPokemonNome:
    def __init__(self):
        sg.ChangeLookAndFeel('DarkGreen1')
        layout=[
            [sg.Text('Nome do Pokemon que deseja selecionar')],
            [sg.Text('Nome'),sg.Input(size=20,key='nome')]
        ]

        self.janela = sg.Window('Nome pokemon').Layout(layout)

    def abrir(self):
        while True:
            evento, valores = self.janela.Read()
            return evento, valores

