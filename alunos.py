# Módulo com funções e classe Aluno
import hashlib
from utils import salvar_dados, carregar_dados
from login import lista_alunos

CAMINHO_ARQUIVO = 'data/alunos.json'

import json  # Importação do json
from utils import carregar_dados

CAMINHO_ARQUIVO = 'data/alunos.json'

def gerar_hash(senha):
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

def cadastrar_alunos():
    alunos = carregar_dados(CAMINHO_ARQUIVO)

    print("\n=== Cadastro de Usuário ===")
    nome = input("Nome do aluno: ").strip().lower()  # Nome em minúsculas
    idade = input("Idade do aluno: ").strip()

    # Verifica se o aluno já está cadastrado
    if nome in alunos:
        print("Usuário já cadastrado.")
        return

    # Coleta e confirma a senha
    senha = input("Digite a senha: ").strip()
    confirmar_senha = input("Confirme a senha: ").strip()

    if senha != confirmar_senha:
        print("As senhas não coincidem. Tente novamente.")
        return

    # Gera o hash da senha
    senha_hash = gerar_hash(senha)

    # Adiciona o novo aluno ao dicionário
    alunos[nome] = {
        "nome": nome.capitalize(),
        "idade": int(idade),
        "senha": senha_hash
    }

    # Salva os dados no arquivo JSON
    try:
        with open(CAMINHO_ARQUIVO, 'w') as arquivo:
            json.dump(alunos, arquivo, indent=4)  # Usa o json.dump para salvar os dados
        print(f"Usuário '{nome.capitalize()}' cadastrado com sucesso!")
    except IOError:
        print("Erro ao salvar os dados. Tente novamente.")


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
        