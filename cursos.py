# Módulo com cursos e disciplinas
from utils import add_cursos,listar_cursos

def exibir_menu2():
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

def menu_prof():
    print('1. adicionar um cursos')
    print('2. listar os cursos')
    opcao = input('digite um numero: ')
    if opcao =='1':
        add_cursos()
        return
    elif opcao == '2':
        listar_cursos()
        return
    else:
        print("opção invalida")
        return