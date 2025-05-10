# Módulo com cursos e disciplinas
def exibir_menu():
    print("\n=== MENU DE CURSOS E DISCIPLINAS ===")
    print("1. Tecnologia da Informação e Comunicação")
    print("2. Matemática e Estatística")
    print("3. Pensamento Lógico Computacional com Python")
    print("4. Infraestrutura Computacional")
    print("5. Lei Geral de Proteção de Dados")
    print("6. Ética, Cidadania e Sustentabilidade")
    print("7. Direitos Humanos")
    print("8. Cibersegurança")
    print("0. Sair")

def selecionar_disciplina(opcao):
    disciplinas = {
        1: "Tecnologia da Informação e Comunicação",
        2: "Matemática e Estatística",
        3: "Pensamento Lógico Computacional com Python",
        4: "Infraestrutura Computacional",
        5: "Lei Geral de Proteção de Dados",
        6: "Ética, Cidadania e Sustentabilidade",
        7: "Direitos Humanos",
        8: "Cibersegurança"
    }
    return disciplinas.get(opcao, None)

while True:
    exibir_menu()
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
