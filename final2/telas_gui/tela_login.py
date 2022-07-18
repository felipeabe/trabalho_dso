import PySimpleGUI as sg

class TelaLogin:
    def __init__(self):
        self.__janela=None
        self.menu()

    def dados_login(self):
        self.menu()
        evento,valores=self.__janela.Read()
        #NÃO ESTA FUNCIONANDO
        if evento=='sair' or sg.WIN_CLOSED:
            self.fechar()

        cadastro={'usuario': valores['usuario'],'idpokedex': valores['idpokedex']}
        self.fechar()
        return cadastro


    def menu(self):
        layout=[
            [sg.Text('Usuario',size=10),sg.Input(key='usuario')],
            [sg.Text('IDpokedex',size=10),sg.Input(key='idpokedex')],
            [sg.Button('Login',key='login'), sg.Button('Sair',key='sair')]
        ]

        self.__janela=sg.Window('Tela de login').layout(layout)


    def fechar(self):
        self.__janela.Close()


