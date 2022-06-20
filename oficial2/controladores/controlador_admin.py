from oficial2.view.tela_admin import TelaAdmin
from oficial2.entidade.treinador import Treinador
from oficial2.view.tela_pokemon import TelaPokemon
from oficial2.controladores.controlador_item import ControleItem

class ControleTreinador:

    def __init__(self, controlador_sistema):
        self.__treinadores = []
        self.__tela_treinador = TelaAdmin()
        self.__tela_pokemon=TelaPokemon()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_item=ControleItem(self)


    @property
    def treinadores(self):
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
        cont=0
        for treinador in self.treinadores:
            if treinador.idpokedex==idpokedex:
                cont+=1
        if cont==0:
            treinador=Treinador(nome,idpokedex)
            self.__treinadores.append(treinador)
        else:
            print('ERRO!')



    def lista_treinadores(self):
        sit=True
        for treinador in self.__treinadores:
            self.__tela_treinador.mostra_treinador({"nome": treinador.nome, "idpokedex": treinador.idpokedex})
            sit=False
        if sit==True:
            print('Não foram registrados treinadores no sistema')

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
            self.__tela_treinador.mostra_mensagem("ATENCAO! Esse treinador não existe")


    def excluir_treinador(self):
        self.lista_treinadores()
        idpokedex = self.__tela_treinador.seleciona_treinador()
        treiandor= self.pega_treinador_por_idpokedex(idpokedex)
        if (treiandor is not None):
            self.__treinadores.remove(treiandor)
            self.lista_treinadores()
        else:
            self.__tela_treinador.mostra_mensagem("ATENCAO! Esse treinador não existe")


    def valida_treinador(self,nome,idpokedex):
        for treinador in self.__treinadores:
            if treinador.nome==nome and treinador.idpokedex==int(idpokedex):
                return treinador

    def ver_todos_pokemons(self):
        sit=True
        for treinador in self.__treinadores:
            for pokemon in treinador.lista_pokemons:
                print("-"*40)
                print(f'Treinador: {treinador.nome}: {pokemon.nome} ,nível {pokemon.level}')
                sit = False
        if sit == True:
            print('Não foram registrados capturas de pokemon no sistema')

    def ver_pokemon_por_nome(self):
        nome=self.__tela_pokemon.nome()
        sit=False
        for treinador in self.__treinadores:
            for pokemon in treinador.lista_pokemons:
                if pokemon.nome==nome:
                    sit=True
                    print("-" * 30)
                    texto=(f'Treinador: {treinador.nome}:{pokemon.nome} ,nível {pokemon.level}')
                    print(texto)
                    break
        if sit==False:
            texto='Não foram registrados capturas desse pokemon'
            print(texto)


    def gerenciar_itens(self):
        self.__controlador_item.abre_tela()


    def retornar(self):
        self.__controlador_sistema.entrar()


    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_treinador, 2: self.alterar_treinador, 4: self.excluir_treinador, 3: self.lista_treinadores,
                         0: self.retornar,5: self.ver_todos_pokemons,6:self.ver_pokemon_por_nome,7:self.gerenciar_itens}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_treinador.tela_opcoes()]
            opcao_escolhida()