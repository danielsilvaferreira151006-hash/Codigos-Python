[ex5.py](https://github.com/user-attachments/files/22373567/ex5.py)
from dateclasses import dateclass
from datetime import datetime

@dataclass
class CadastroCliente:
nome:str
email:str
telefone:str

def menu():
    print("\n--- Barbearia Cortes Profundos ---")
    print("1 - Cadastro Cliente ")
    print("2- Cadastro Barbeiro ")
    print("3- Agendamento de Serviço")
    print("4- Cancelar Agendamento" )
    print("5- Sair ")
    return input ("Escolha Uma Opção:")
 



while True:    
    if opcao == "1":  
        
