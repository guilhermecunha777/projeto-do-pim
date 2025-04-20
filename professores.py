# Módulo com funções e classe Professor
from utils import salvar_dados, carregar_dados

CAMINHO_ARQUIVO = 'data/professores.json'

def cadastrar_professor():
    nome = input("nome do professor: ")
    disciplina = input("disciplina: ")
    
    professores = carregar_dados(CAMINHO_ARQUIVO)
    professores.append({
        "nome": nome,
        "disciplina": disciplina
    })
    salvar_dados(CAMINHO_ARQUIVO, professores)
    print("professor cadastrado com sucesso!")

def lista_professores():
    professores = carregar_dados(CAMINHO_ARQUIVO)
    if not professores:
        print("nenhum professor cadastrado.")
        return
    for idx, prof in enumerate(professores, start=1):
        print(f"{idx}. {prof['nome']} | disciplina: {prof['disciplina']} ")

def remover_professores():
    lista_professores()
    professores = carregar_dados(CAMINHO_ARQUIVO)
    try:
        indice = int(input("digite o numero do professor a remover: ")) -1
        if 0 <= indice < len(professores):
            removido = professores.pop(indice)
            salvar_dados(CAMINHO_ARQUIVO, professores)
            print(f"professor {removido['nome']} removido com sucesso.")
        else:
            print("indice invalido.")
    except ValueError:
        print("entrada invalida.")
