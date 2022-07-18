import PySimpleGUI as sg

class TelaUsuario:
    def __init__(self):
        layout=[
            [sg.Text('Selcione sua opção',font=50)],
            [sg.Radio('Gerenciar pokemons','opcao', key='pokemons',font=35)],
            [sg.Radio('Relatórios','opcao', key='relatorios',font=35)],
            [sg.Radio('Gerenciar Mochila', 'opcao', key='mochila',font=35)],
            [sg.Button('Continuar', key='opcao', font=35), sg.Button('Voltar', key='voltar', font=35)]
        ]

        self.janela=sg.Window('Tela Usuario').Layout(layout)

    def abrir(self):
        while True:
            evento, valores=self.janela.Read()
            return evento, valores


    def fechar(self):
        self.janela.Close()