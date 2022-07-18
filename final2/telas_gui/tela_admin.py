import PySimpleGUI as sg

class TelaAdmin:
    def __init__(self):
        self.__janela=None
        self.menu()


    def tela_opcoes(self):
        self.menu()
        evento,valores=self.janela.Read()
        opcao=0
        if valores['incluir']:
            opcao=1
        if valores['excluir']:
            opcao=2
        if valores['alterar']:
            opcao=3
        if valores['listar']:
            opcao=3
        if evento=='voltar':
            opcao=0
        self.fechar()
        return opcao


    def menu(self):
        layout=[
            [sg.Text('Selcione sua opção',font=50)],
            [sg.Radio('Incluir Treinador','opcao', key='incluir',font=35)],
            [sg.Radio('Excluir Treinador','opcao', key='excluir',font=35)],
            [sg.Radio('Alterar Treinador', 'opcao', key='alterar',font=35)],
            [sg.Radio('Listar Treinadores', 'opcao', key='listar',font=35)],
            [sg.Radio('Ver todos os pokemons registrados no sistema','opcao',key='pokemons',font=35)],
            [sg.Radio('Gerenciar itens', 'opcao', key='itens',font=35)],
            [sg.Radio('Pesquisar pokemon por nome', 'opcao', key='pokemon_nome',font=35)],
            [sg.Button('Continuar',key='opcao',font=35),sg.Button('Voltar',key='voltar',font=35)]
        ]
        self.janela=sg.Window('Tela admin').Layout(layout)


    def abrir(self):
        evento, valores=self.janela.Read()
        return evento, valores

    def fechar(self):
        self.janela.Close()