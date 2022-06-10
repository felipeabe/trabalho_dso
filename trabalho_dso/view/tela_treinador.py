class TelaTreinador:

    def tela_opcoes(self):
        print("------TREINADORES------")
        print('1 - Adicionar treinador')
        print('2 - Alterar treinador')
        print('3 - Remover treinador')
        print('4 - Listar treinadores')
        print('5 - Abrir mochila do treinador')
        print('6 - Ver lista de pokemons do treinador')
        print('7 - Transferir pokemon')
        print('8 - Retornar')

        opcao = int(input("Escolha a opcao: "))
        return opcao

    def dados_treinador(self):
        print('-----DADOS TREINADOR-----')
        nome=str(input('NOME do treinador: '))
        idpokedex=int(input('Idpokedex: '))
        return {"nome":nome, "idpokedex":idpokedex}

    def mostra_treinador(self, dados_treinador):
        print("NOME DO TREINADOR: ", dados_treinador["nome"])
        print("IDPOKEDEX DO TREINADOR: ", dados_treinador["idpokedex"])
        print("\n")


    def seleciona_treinador(self):
        idpokedex = int(input("Idpokedex do treinador que deseja selecionar: "))
        return idpokedex

    def mostra_mensagem(self, mensagem):
        print(mensagem)

