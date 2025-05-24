# Módulo com cursos e disciplinas
from utils import add_cursos,listar_cursos

caminho = 'data/cursos.json'

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

def buscar_curso_por_nome():#não fui add
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            cursos= json.load(f)
    except FileNotFoundError:
        print("erro ao decodificar o arquivo JSON.")
        return
    
    nome_buscar = input("Digite o nome (ou parte do nome) do curso que deseja buscar: ").strip().lower()

    encontrados = [curso for curso in cursos if nome_buscar in curso["nome"].lower()]

    if encontrados:
        print("\nCursos encontrados: ")
        for curso in encontrados:
            print(f"ID:{curso['id']}, nome: {curso['nome']}, conteudo: {curso['conteudo']}")
    else:
        print("nenhum curso encontrado com esse nome.")

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