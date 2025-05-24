# Módulo com funções e classe Professor
import json
import hashlib
from utils import salvar_dados, carregar_dados
from login import lista_professores ,carregar_professor ,salvar_professor

CAMINHO_ARQUIVO = 'data/professores.json'

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def cadastrar_professor():
    professores = carregar_professor()
    nome = input("nome do professor: ").strip()
    senha = input("digite a senha: ").strip()
    disciplina = input("disciplina: ").strip()
    senha_hash = gerar_hash(senha)
    
    if professores:
        ultimo_id = max(p["id"] for p in professores.values())
        novo_id = ultimo_id + 1
    else:
        novo_id = 1

    professores[nome] = {
        "id": novo_id,
        "senha": senha_hash,
        "disciplina": disciplina 
    }
    salvar_professor(professores)
    print(f"professor cadastrado com sucesso! ID: {novo_id}")

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
