from final.view.tela_sistema import TelaSistema
from final.view.tela_login import TelaLogin
from final.controladores.controlador_admin import ControleTreinador
from final.view.tela_admin import TelaAdmin
from final.view.tela_usuario import TelaUsuario
from final.controladores.controlador_pokemon import ControladorPokemon
from final.controladores.controlador_relatorios import ControladorRelatorios
from final.telas_gui.tela_login import TelaLogin

class ControladorSistema:


    def __init__(self):
        self.__tela_sistema=TelaSistema()
        self.__tela_admin=TelaAdmin()
        self.__controlador_admin=ControleTreinador(self)
        self.__tela_usuario=TelaUsuario()
        self.__controlador_pokemon=ControladorPokemon(self)
        self.__controlador_relatorios=ControladorRelatorios(self)
        self.__usuario_logado=None
        self.__tela_login = TelaLogin()


    @property
    def usuario_logado(self):
        return self.__usuario_logado


    def inicializa_sistema(self):
        self.entrar()


    def entrar(self):
        self.__usuario_logado=None
        situacao = False
        while situacao == False:

            evento, valores = self.__tela_login.abrir()
            if valores['usuario'] == "admin" and valores['idpokedex'] == 'admin' and valores['usuario'] and valores['idpokedex']:
                self.__tela_login.fechar()
                self.__controlador_admin.abre_tela()

            else:
                self.__usuario_logado=self.__controlador_admin.valida_treinador(valores["usuario"],valores["idpokedex"])
                if not self.__usuario_logado:
                    self.__tela_admin.mostra_mensagem('Dados incorretos')
                else:
                    situacao = True
                    lista_opcoes = {1: self.gerenciar_pokemons, 2: self.relatorios}
                    while True:
                        opcao_escolhida = self.__tela_usuario.tela_opcoes()
                        funcao_escolhida = lista_opcoes[opcao_escolhida]
                        funcao_escolhida()
                        break






    def gerenciar_pokemons(self):
        self.__controlador_pokemon.abre_tela()

    def relatorios(self):
        self.__controlador_relatorios.abre_tela_relatorios()

