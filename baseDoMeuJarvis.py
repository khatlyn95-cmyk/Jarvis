from datetime import datetime

def iniciar_jarvis():
    print("J.A.R.V.I.S. Online")
    print("Digite ajuda, hora ou sair")

    while True:
        comando = input("Você > ").strip().lower()

        if comando == "ajuda":
            print("Comandos: ajuda, hora, sair")
            
        elif comando == "hora":
            print(datetime.now().strftime("%H:%M:%S"))
        
        elif comando == "sair":
            print("JARVIS Encerrado.")
            break
        
        else:
            print("Comando não reconhecido.")

if __name__ == "__main__":
    iniciar_jarvis()