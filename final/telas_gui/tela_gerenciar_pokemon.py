import PySimpleGUI as sg

class TelaGereciarPokemons:
    def __init__(self):
        layout=[
            [sg.Radio('Capturar pokemon', 'opcao', key='capturar', font=35)],
            [sg.Radio('Excluir pokemon', 'opcao', key='excluir', font=35)],
            [sg.Radio('Alterar pokemon', 'opcao', key='alterar', font=35)],
            [sg.Radio('Listar pokemon', 'opcao', key='listar', font=35)],
            [sg.Button('Continuar'), sg.Button('Voltar',key='voltar')]
        ]

        self.janela = sg.Window('Gerenciar pokemons').Layout(layout)

    def abrir(self):
        while True:
            evento, valores=self.janela.Read()
            return evento, valores



