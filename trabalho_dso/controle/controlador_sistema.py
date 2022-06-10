from trabalho_dso.view.tela_sistema import TelaSistema
from trabalho_dso.controle.controlador_treinador import ControleTreinador
from trabalho_dso.controle.controlador_pokemon import ControladorPokemon


class ControladorSistema:

    def __init__(self):
        self.__controlador_treinadores = ControleTreinador(self)
        self.__controlador_pokemons = ControladorPokemon(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_treinadores(self):
        return self.__controlador_treinadores

    @property
    def controlador_pokemons(self):
        return self.__controlador_pokemons

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_treinadores(self):
        self.__controlador_treinadores.abre_tela()

    def cadastra_pokemons(self):
        # Chama o controlador de Amigos
        self.__controlador_pokemons.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_treinadores, 2: self.cadastra_pokemons,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()