# Módulo com funções e classe Aluno
from utils import salvar_dados, carregar_dados
from login import lista_alunos

CAMINHO_ARQUIVO = 'data/alunos.json'

def cadastrar_alunos():
    nome = input("nome do aluno: ")
    idade = input("idade: ")
    senha = input("senha: ")
    
    alunos = carregar_dados(CAMINHO_ARQUIVO)
    alunos.append({
        "nome": nome,
        "idade": idade,
        "senha": senha
    })
    salvar_dados(CAMINHO_ARQUIVO, alunos)
    print("aluno cadastrado com sucesso!")


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
        