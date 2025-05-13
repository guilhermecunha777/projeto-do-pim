# Módulo com funções e classe Aluno
import json
import hashlib
from utils import salvar_dados, carregar_dados
from login import lista_alunos, carregar_usuarios, salvar_usuarios

CAMINHO_ARQUIVO = 'data/alunos.json'

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar_alunos():
    usuarios = carregar_usuarios()
    usuario = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()

    if usuario in usuarios:
        print("Usuário já existe. Tente outro nome.")
        return

    senha_hash = gerar_hash(senha)
    usuarios[usuario] = senha_hash
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

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
        