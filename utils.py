# Funções auxiliares (validações, limpar tela, salvar/carregar dados)
import json
import os

def salvar_dados(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def carregar_dados(caminho):
    try:
        with open(caminho, 'r') as arquivo:
            dados = json.load(arquivo)
            print(dados)
            return dados
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Erro ao carregar os dados: {e}")
        return {}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
