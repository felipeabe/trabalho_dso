from trabalho_dso.entidade.treinador import Treinador
from trabalho_dso.view.tela_pokemon import TelaPokemon
from trabalho_dso.controle.controlador_treinador import ControleTreinador
from trabalho_dso.entidade.pokemon import Pokemon

class ControladorPokemon:

    def __init__(self,controlador_sistema):
        self.__pokemons=[]
        self.__tela_pokemon=TelaPokemon()
        self.__controlador_sistema=controlador_sistema
        self.__controlador_treinador=ControleTreinador(self)


    def capturar_pokemon(self):
        print(self.__controlador_treinador.lista_treinadores_bruta)
        dados_pokemon=self.__tela_pokemon.dados_pokemon()
        treinador=Treinador(dados_pokemon["nome_treinador"],dados_pokemon["id_treinador"])
        nome=dados_pokemon["nome"]
        tipo=dados_pokemon["tipo"]
        level = dados_pokemon["level"]
        ataques=dados_pokemon["ataques"]
        defesa=dados_pokemon["defesa"]
        regiao=dados_pokemon["regiao"]
        pokemon=Pokemon(treinador,nome,tipo,level,ataques,defesa,regiao)
        self.__pokemons.append(pokemon)

        # if int(treinadores.idpokedex)==int(treinador.idpokedex):
        # treinadores.lista_pokemons.append(pokemon)




    def listar_pokemons(self):
        for pokemon in self.__pokemons:
            self.__tela_pokemon.mostra_pokemon({"treinador": pokemon.treinador.nome, "nome": pokemon.nome, "tipo": pokemon.tipo,"level": pokemon.level, "ataques": pokemon.ataques, "defesa": pokemon.defesa, "regiao": pokemon.regiao})

    def retornar(self):
        self.__controlador_sistema.abre_tela()


    def abre_tela(self):
        lista_opcoes = {1: self.capturar_pokemon, 2: self.listar_pokemons,4:self.listar_pokemons,
                        6: self.retornar}
        continua = True
        while continua:
            opcao_escolhida = lista_opcoes[self.__tela_pokemon.tela_opcoes()]
            opcao_escolhida()







