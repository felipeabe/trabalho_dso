from trabalho_dso.entidade.ataques_pokemon import AtaquesPokemon
from trabalho_dso.entidade.treinador import Treinador


class TelaPokemon:


    def tela_opcoes(self):
        print("------POKEMONS------")
        print('1 - Capturar pokemon')
        print('2 - Alterar pokemon')
        print('3 - Remover pokemon')
        print('4 - Listar pokemons')
        print('5 - Evoluir pokemon')
        print('6 - Retornar')

        opcao = int(input("Escolha a opcao: "))
        return opcao


    def dados_pokemon(self):
        print('-----DADOS POKEMON-----')
        nome_treinador=str(input('Nome do treinador: '))
        id_treinador=int(input('Idpokedex do treiandor: '))
        treinador=Treinador(nome_treinador,id_treinador)
        nome=str(input('NOME do Pokemon: '))
        tipo=str(input('Tipo: '))
        level=int(input('Level: '))
        ataques=AtaquesPokemon().ataques
        defesa=int(input('Defesa: '))
        regiao=str(input('Regiao: '))
        return {"nome_treinador":treinador.nome,"id_treinador": treinador.idpokedex,"nome":nome, "tipo":tipo, "level": level, "ataques": ataques, "defesa": defesa, "regiao": regiao}

    def mostra_pokemon(self, dados_pokemon):
        print("Treinador: ", dados_pokemon["treinador"])
        print("Nome do POKEMON: ", dados_pokemon["nome"])
        print("Tipo do POKEMON: ", dados_pokemon["tipo"])
        print("Level do POKEMON: ", dados_pokemon["level"])
        print("Ataques do POKEMON: ", dados_pokemon["ataques"])
        print("Defesa DO POKEMON: ", dados_pokemon["defesa"])
        print("Regiao DO POKEMON: ", dados_pokemon["regiao"])
        print("\n")

    def seleciona_pokemon(self):
        nome = input("Nome do pokemon que deseja selecionar: ")
        return nome


