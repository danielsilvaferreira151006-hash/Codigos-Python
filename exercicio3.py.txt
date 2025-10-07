from dataclasses import dataclass

@dataclass
class Postagem:
    conteudo: str
    descricao: str
    autor: str
    dataEHora: str
    curtida: int

lista = []

def criarPublicacao():
    conteudo = input("\nQual o conteudo: ")
    descricao = input("Qual a descrição: ")
    autor = input("Quem é o autor: ")
    dataEHora = input("Qual a data e a hora: ")
    curtida = 0
    postagem = Postagem(conteudo, descricao, autor, dataEHora, curtida)
    lista.append(postagem)
    print("\nPublicação efetuada com sucesso")



def curtirPublicacao():
    if lista == []:
        print("\nNao ha nenhuma postagem")
    else:
        for num, postagem in enumerate(lista, start = 1):
            print(f"\n{num} - {postagem.descricao} ({postagem.curtida} curtidas)")
        escolha = int(input("\nDigite o número da publicação que deseja curtir: "))
        if 1 <= escolha <= len(lista):
            lista[escolha - 1].curtida += 1
            print("\nVocê curtiu a publicação!")
        else:
            print("\nOpção inválida")



def verPublicacao():
    if lista == []:
        print("\nNao ha nenhuma postagem")
    else:
        for postagem in lista:
            print(postagem)


def verPublicacaoI():
    if lista == []:
        print("Nao ha nenhuma postagem")
    else:
        for num, postagem in enumerate(lista, start = 1):
            print(f"\n{num} - {postagem.descricao}")
        
        escolha = int(input("\nDigite o número da publicação que deseja ver: "))
        if 1 <= escolha <= len(lista):
            publi = lista[escolha - 1]
            print("\n--- Publicacao individual ---")
            print(f"Autor: {publi.autor}")
            print(f"Descrição: {publi.descricao}")
            print(f"Conteúdo: {publi.conteudo}")
            print(f"Data e Hora: {publi.dataEHora}")
            print(f"Curtidas: {publi.curtida}")
    
def menu():
    print("\n --- Instagram 2.0 --- ")
    print("1- Criar Publicacao")
    print("2- Curtir Publicações")
    print("3- Ver todas as publicações")
    print("4- Ver Publicação Especifica")
    print("5- Sair")
    return input("\nDigite a opção: ")

while True:
    opcao = menu()
    if opcao == "1":
        criarPublicacao()
    
    elif opcao == "2":
        curtirPublicacao()
        
    elif opcao == "3":
        verPublicacao()

    elif opcao == "4":
        verPublicacaoI()
        
    elif opcao == "5":
        break

    else:
        print("\nEscreve algo que preste")