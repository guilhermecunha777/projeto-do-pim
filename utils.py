# Funções auxiliares (validações, limpar tela, salvar/carregar dados)
import json
import os

def salvar_dados(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def carregar_dados(caminho):
    if not os.path.exists(caminho):
        print(f"Arquivo '{caminho}' não encontrado. Criando um novo arquivo.")
        return []

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            if os.path.getsize(caminho) == 0:
                print(f"Arquivo '{caminho}' está vazio. Retornando lista vazia.")
                return []
            return json.load(arquivo)
    except json.JSONDecodeError:
        print(f"Erro ao ler o arquivo '{caminho}'. O arquivo não está em formato JSON válido.")
        return []


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
