# Arquivo principal que executa o menu do sistema
from alunos import cadastrar_alunos
from login import autenticar_usuario
from cursos import exibir_menu2, selecionar_disciplina

def exibir_menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Login")
        print("2 - Cadastrar")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            if autenticar_usuario():
                while True:
                    exibir_menu2()
                    try:
                        escolha2 = int(input("Selecione uma disciplina (0 para voltar): "))
                        if escolha2 == 0:
                            print("Voltando ao menu principal...")
                            break
                        disciplina = selecionar_disciplina(escolha2)
                        if disciplina:
                            print(f"Você selecionou: {disciplina}")
                        else:
                            print("Opção inválida. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Digite um número.")
        
        elif escolha == "2":
            cadastrar_alunos()
            
        elif escolha == "0":
            print("Encerrando o sistema.")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    exibir_menu()
