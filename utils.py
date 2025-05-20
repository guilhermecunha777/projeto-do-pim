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

caminho = 'data/cursos.json'

def add_cursos():
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            cursos = json.loads(f)
    except:
        cursos = []
    
    id_atual = max([c.get("id", 0) for c in cursos], default=0)
    
    nome = input("nome do cursos: ")
    conteudo = input("qual é o conteudo do cursos: ")
    
    novo_cursos = {"id":id_atual + 1, "nome": nome, "conteudo":conteudo}
    cursos.append(novo_cursos)
    
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(cursos, f, indent=2, ensure_ascii=False)
    print("curso adicionado com sucesso!")

def listar_cursos():
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            cursos = json.loads(f)
    except:
        cursos = []
    
    if not cursos:
        print("nenhum curso cadastrados")
    else:
        print("cursos cadastrados")
        for cursos in cursos:
            print(f"ID: {cursos['id']} | nome: {cursos['nome']} | conteudo: {cursos['conteudo']} ")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
