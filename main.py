from alunos import cadastrar_alunos
from professores import cadastrar_professor
from login import autenticar_usuario, autenticar_professor

def exibir_menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Login")
        print("2 - Login do professor")
        print("3 - Cadastrar do aluno")
        print("4 - Cadastrar do professor")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            autenticar_usuario()
        elif escolha == "2":
            autenticar_professor()
        elif escolha == "3":
            cadastrar_alunos()
        elif escolha == "4":
            cadastrar_professor()
        elif escolha == "0":
            print("Encerrando o sistema.")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    exibir_menu()
