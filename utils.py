# Funções auxiliares (validações, limpar tela, salvar/carregar dados)
import json
import os

def salvar_dados(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def carregar_dados(caminho):
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.loas(arquivo)
    return []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
