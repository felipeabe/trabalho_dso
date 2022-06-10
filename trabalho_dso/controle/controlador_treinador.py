from trabalho_dso.view.tela_treinador import TelaTreinador
from trabalho_dso.entidade.treinador import Treinador

class ControleTreinador:

    def __init__(self, controlador_sistema):
        self.__treinadores = []
        self.__tela_treinador = TelaTreinador()
        self.__controlador_sistema = controlador_sistema

    @property
    def lista_treinadores_bruta(self):
        return self.__treinadores

    def pega_treinador_por_idpokedex(self, idpokedex: int):
        for treinador in self.__treinadores:
            if (treinador.idpokedex == idpokedex):
                return treinador
        return None

    def adicionar_treinador(self):
        dados_treinador=self.__tela_treinador.dados_treinador()
        nome=dados_treinador["nome"]
        idpokedex=dados_treinador["idpokedex"]
        treinador=Treinador(nome,idpokedex)
        self.__treinadores.append(treinador)


    def lista_treinadores(self):
        for treinador in self.__treinadores:
            self.__tela_treinador.mostra_treinador({"nome": treinador.nome, "idpokedex": treinador.idpokedex})
            print(treinador.idpokedex)

    def alterar_treinador(self):
        self.lista_treinadores()
        idpokedex = self.__tela_treinador.seleciona_treinador()
        treinador = self.pega_treinador_por_idpokedex(idpokedex)

        if (treinador is not None):
            novos_dados_treinador = self.__tela_treinador.dados_treinador()
            treinador.nome = novos_dados_treinador["nome"]
            treinador.idpokedex = novos_dados_treinador["idpokedex"]
            self.lista_treinadores()
        else:
            self.__tela_treinador.mostra_mensagem("ATENCAO: Esse treinador não existe")


    def excluir_treinador(self):
        self.lista_treinadores()
        idpokedex = self.__tela_treinador.seleciona_treinador()
        treiandor= self.pega_treinador_por_idpokedex(idpokedex)

        if (treiandor is not None):
            self.__treinadores.remove(treiandor)
            self.lista_treinadores()
        else:
            self.__tela_treinador.mostra_mensagem("ATENCAO: Esse treinador não existe")


    def acessar_lista_pokemons(self):
        idpokedex=self.__tela_treinador.seleciona_treinador()
        for treinador in self.__treinadores:
            if idpokedex == treinador.idpokedex:
                 print(treinador.lista_pokemons)
            else:
                 print('porra')

    def acessar_mochila(self):
        pass


    def transferir_pokemon(self,de,para,pokemon):
        pass


    def retornar(self):
        self.__controlador_sistema.abre_tela()


    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_treinador, 2: self.alterar_treinador, 3: self.excluir_treinador, 4: self.lista_treinadores,
                        6:self.acessar_lista_pokemons ,8: self.retornar}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_treinador.tela_opcoes()]
            opcao_escolhida()