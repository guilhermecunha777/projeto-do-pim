import json
import hashlib
import os
from utils import carregar_dados

CAMINHO_ARQUIVO = 'data/alunos.json'

def gerar_hash(senha):
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

def carregar_dados(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Erro ao carregar os dados dos usuários.")
        return {}

def autenticar_usuario():
    alunos = carregar_dados(CAMINHO_ARQUIVO)
    nome = input("Usuário: ").strip().lower()
    senha = input("Senha: ").strip()

    if nome in alunos and alunos[nome] == gerar_hash(senha):
        print(f"Login bem-sucedido. Bem-vindo, {nome}!")
    else:
        print("Usuário ou senha incorretos.")

def lista_alunos():
    alunos = carregar_dados(CAMINHO_ARQUIVO)
    if not alunos:
        print("nenhum aluno cadastrado.")
        return
    for idx, aluno in enumerate(alunos, start=1):
        print(f"{idx}. {aluno['nome']} | Idade: {aluno['idade']} |senha: {aluno['senha']}")
