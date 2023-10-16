import requests
import os
from colorama import init, Fore, Back, Style

init()

SERVIDOR_URL = 'http://127.0.0.1:5555'

#add usuario no json de envio, depois usuario que fez msg no obj, e depois fazer tudo isso funcionar. 
def enviar_mensagem(usuario):

    response = requests.get(f'{SERVIDOR_URL}/usuario')
    usuarios = response.json()['usuarios']

    if(len(usuarios) == 1):
        print(Fore.RED  + "Só há 1 único usuário no sistema!\n Não é possível mandar mensagens!" + Fore.RESET)
        return

    for u in usuarios:
        print(u['nome'])

    usuarioFinal = input("Para quem é sua mensagem?")
    msg = input("Digite sua mensagem: ")

    msg = str.format(f"{usuario}: {msg}")

    resposta = requests.post(f'{SERVIDOR_URL}/enviar', json={'mensagem': msg, 
                                                             'usuario': usuario, 
                                                             'usuarioFinal': usuarioFinal})

    limpar_tela()

    print(resposta.json()['status'])
    print("Exibindo mensagens...")

    receber_mensagens()

def receber_mensagens():
    resposta = requests.get(f'{SERVIDOR_URL}/receber')
    mensagens = resposta.json()['mensagens']
    print("Mensagens recebidas:")
    print(Fore.CYAN + "-" * 20 + Fore.RESET)
    for msg in mensagens:
        print(Fore.BLACK + Back.LIGHTWHITE_EX + f"- {msg}" + Fore.RESET + Back.RESET)
    print(Fore.CYAN + "-" * 20 + Fore.RESET)

def criarUsuario():

    usuario = input("Informe seu nome de usuário: \n>> ")
    
    
    while(usuario == ""):
        limpar_tela()
        print("Seu nome de usuário é vazio!")
        print("Você precisa ter um nome de usuário! Tente novamente")
        usuario = input("Informe seu nome de usuário: \n>> ")
        
    response = requests.post(f'{SERVIDOR_URL}/usuario', json={'nome': usuario})

    limpar_tela()
    print(response.json()['status'] + '\n')

    return usuario
    

def print_opcao_invalida():
    print("Opção inválida! Por favor, tente novamente")


def sair_programa():
    sair = input("Você deseja sair do programa? (s/n)\n>> ")
    
    match sair.lower():
        case 's':
            print("Obrigado por utilizar o programa :)")
            return False
        case 'n':
            print("Voltando ao programa...")
            return True
            
        case default:
            print_opcao_invalida()
            return True
        
def limpar_tela():
    os.system('cls')
    

if __name__ == '__main__':
    continuar = True

    usuario = criarUsuario()

    while continuar:
        print(f"Olá, {usuario}")
        print("1. Enviar mensagem")
        print("2. Receber mensagens")
        print("3. Sair do programa")
        escolha = input("Escolha uma opção:\n>> ")
        
        match escolha:
            case '1':
                limpar_tela()
                enviar_mensagem(usuario)
                
            case '2':
                limpar_tela()
                receber_mensagens()
            case '3':
                limpar_tela()
                continuar = sair_programa()
                  
            case default:
                limpar_tela()
                print_opcao_invalida()
                

        


#TODO Adicione a tag <nome> do utilizador em cada mensagem enviada (FEITO)
#TODO - Uma opção para sair do programa (FEITO)
#TODO - Após enviar a mensagem automaticamente limpar a tela e exibir toda a conversa novamente (FEITO)