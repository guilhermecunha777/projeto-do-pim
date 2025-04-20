# Módulo com funções e classe Aluno
from utils import salvar_dados, carregar_dados

CAMINHO_ARQUIVO = 'data/alunos.json'

def cadastrar_alunos():
    nome = input("nome do aluno: ")
    idade = input("idade: ")
    matricula = input("matrícula: ")
    
    alunos = carregar_dados(CAMINHO_ARQUIVO)
    alunos.append({
        "nome": nome,
        "idade": idade,
        "matricula": matricula
    })
    salvar_dados(CAMINHO_ARQUIVO, alunos)
    print("aluno cadastrado com sucesso!")

def lista_alunos():
    alunos = carregar_dados(CAMINHO_ARQUIVO)
    if not alunos:
        print("nenhum aluno cadastrado.")
        return
    for idx, aluno in enumerate(alunos, start=1):
        print(f"{idx}. {aluno['nome']} | Idade: {aluno['idade']} | matrícula: {aluno['matricula']}")

def remover_aluno():
    lista_alunos()
    alunos = carregar_dados(CAMINHO_ARQUIVO)
    try:
        indice = int(input("digite o numero do alunoa remover: ")) -1
        if 0 <= indice < len(alunos):
            removido = alunos.pop(indice)
            salvar_dados(CAMINHO_ARQUIVO, alunos)
            print(f"aluno {removido['nome']} removido com sucesso.")
        else:
            print("indice inválido.")
    except ValueError:
        print("entrada inválida.")