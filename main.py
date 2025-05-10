# Arquivo principal que executa o menu do sistema
from login import autenticar_usuario
from alunos import cadastrar_alunos
from cursos import exibir_menu2, selecionar_disciplina

def exibir_menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Login")
        print("2 - Cadastrar")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            # if autenticar_usuario() == True:
                while True:
                    exibir_menu2()
                    try:
                        escolha = int(input("Selecione uma opção (0 para sair): "))
                        if escolha == 0:
                            print("Saindo do programa. Até logo!")
                            break
                        disciplina = selecionar_disciplina(escolha)
                        if disciplina:
                            print(f"Você selecionou: {disciplina}")
                        else:
                            print("Opção inválida. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Digite um número correspondente à opção.")
        
        elif escolha == "2":
            cadastrar_alunos()
            
        elif escolha == "0":
            print("Encerrando o sistema.")
            break
        
        else:
            print("Opção inválida.")

# Execução principal

if __name__ == "__main__":
    exibir_menu()
