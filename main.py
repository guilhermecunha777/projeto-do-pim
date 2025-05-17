# Arquivo principal que executa o menu do sistema
from alunos import cadastrar_alunos
from login import autenticar_usuario

def exibir_menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Login")
        print("2 - Cadastrar")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            autenticar_usuario()
        elif escolha == "2":
            cadastrar_alunos()
        elif escolha == "0":
            print("Encerrando o sistema.")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    exibir_menu()
