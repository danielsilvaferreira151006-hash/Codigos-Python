#Exercício 1.2
#Bilheteria de evento com apenas 1 evento.
#1.Cadastrar nome do evento.
#2.Vender Ingressos(verificar se há ingressos suficientes).
#3.Repor ingresso(quantidade>0).
#4.Ver Ingressos disponíveis.

def menu():
    print("\n--- TicketMaster---")
    print("1- Registrar Show ")
    print("2- Venda de Ingressos")
    print("3- Adicionar Ingressos")
    print("4- Ver Ingressos disponíveis")
    print("0- Sair da pagina de venda")
    return input("Escolha uma opção: ")
ingresso = None
quantidade = 0

while True:
    opcao = menu()

    if opcao == "1":
        ingresso = input("Digite nome do Show: ")
        quantidade = 0
        print(f"Produto '{ingresso}' cadastrado com sucesso!")

    elif opcao == "2":
        if ingresso is None:
            print("Nenhum ingresso cadastrado ainda!")
        else:
            retirar = int(input("Digite a quantidade de ingressos a retirar: "))
            if retirar <= 0:
                print("A quantidade de ingressos deve ser maior que zero!")
            elif retirar > quantidade:
                print("Quantidade de ingresso insuficiente no estoque!")
            else:
                quantidade -= retirar
                print(f"Retirado {retirar} unidade(s). Estoque atual: {quantidade}")

    elif opcao == "3":
        if produto is None:
            print("Nenhum ingresso cadastrado ainda!")
        else:
            adicionar = int(input("Digite a quantidade de ingresso a adicionar: "))
            if adicionar <= 0:
                print("A quantidade de ingresso deve ser maior que zero!")
            else:
                quantidade += adicionar
                print(f"Adicionado {adicionar} unidade(s). Estoque atual: {quantidade}")

    elif opcao == "4":
        if produto is None:
            print("Nenhum ingresso cadastrado ainda!")
        else:
            print(f"Produto: {produto} | Quantidade em estoque: {quantidade}")

    elif opcao == "0":
        print("Saindo de TicketMaster ... até mais!")
        break

    else:
        print("Opção inválida! Tente novamente.")
    
    