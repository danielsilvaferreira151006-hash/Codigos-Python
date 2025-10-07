from dataclasses import dataclass
import datetime

@dataclass
class Usuario:
    nome_completo: str
    endereco_email: str
    senha_acesso: str

@dataclass
class Publicacao:
    texto: str
    legenda: str
    criador: Usuario
    momento: datetime.datetime
    qtd_curtidas: int = 0

banco_usuarios = []
banco_publicacoes = []
esta_autenticado = False
usuario_atual = None

def processar_login():
    """Gerencia o processo de autenticação do usuário."""
    global esta_autenticado, usuario_atual
    email_informado = input("\nInforme seu email: ")
    senha_informada = input("Informe sua senha: ")
    
    for usuario in banco_usuarios:
        if usuario.endereco_email == email_informado and usuario.senha_acesso == senha_informada:
            print("\nLogin realizado com sucesso!")
            esta_autenticado = True
            usuario_atual = usuario
            return
    
    print("\nEmail ou senha inválidos.")

def cadastrar_novo_usuario():
    """Cria uma nova conta de usuário e realiza o login automaticamente."""
    global esta_autenticado, usuario_atual
    print("\nVamos criar sua conta.")
    nome_usuario = input("Digite seu nome completo: ")
    email_usuario = input("Digite seu email: ")
    senha_usuario = input("Digite sua senha: ")
    
    novo_usuario = Usuario(nome_usuario, email_usuario, senha_usuario)
    banco_usuarios.append(novo_usuario)
    esta_autenticado = True
    usuario_atual = novo_usuario
    print("Conta criada com sucesso!")

def exibir_menu_principal():
    """Mostra o menu principal e processa as escolhas do usuário."""
    global esta_autenticado, usuario_atual
    
    while True:
        if not banco_usuarios:
            cadastrar_novo_usuario()
        elif not esta_autenticado:
            processar_login()
        else:
            print("\n=== Rede Social Simples === ")
            print("1 - Criar uma nova publicação")
            print("2 - Curtir publicações")
            print("3 - Visualizar todas as publicações")
            print("4 - Visualizar publicação específica")
            print("5 - Sair da conta")
            
            opcao = input("\nEscolha uma opção (1-5): ").strip()
            
            if opcao == "1":
                conteudo_post = input("\nQual é o conteúdo da publicação? ")
                legenda_post = input("Adicione uma legenda: ")
                tempo_atual = datetime.datetime.now()
                nova_publicacao = Publicacao(conteudo_post, legenda_post, usuario_atual, tempo_atual)
                banco_publicacoes.append(nova_publicacao)
                print("\nPublicação criada com sucesso!")
            
            elif opcao == "2":
                print("Essa funcionalidade será implementada em breve.")
            
            elif opcao == "3":
                if not banco_publicacoes:
                    print("\nNenhuma publicação disponível ainda.")
                else:
                    for publicacao in banco_publicacoes:
                        print(f"\nCriado por: {publicacao.criador.nome_completo}")
                        print(f"Conteúdo: {publicacao.texto}")
                        print(f"Legenda: {publicacao.legenda}")
                        print(f"Momento: {publicacao.momento}")
                        print(f"Curtidas: {publicacao.qtd_curtidas}")
            
            elif opcao == "4":
                print("Essa funcionalidade será implementada em breve.")
            
            elif opcao == "5":
                esta_autenticado = False
                usuario_atual = None
                print("Você saiu da conta com sucesso.")
            
            else:
                print("\nPor favor, selecione uma opção válida.")

if __name__ == "__main__":
    exibir_menu_principal()

