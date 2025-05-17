import json
import hashlib
import os
from utils import carregar_dados
from cursos import exibir_menu2,selecionar_disciplina

CAMINHO_ARQUIVO = 'data/alunos.json'

def gerar_hash(senha):
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

def carregar_usuarios():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return {}
    with open(CAMINHO_ARQUIVO, "r") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return {}

def salvar_usuarios(usuarios):
    with open(CAMINHO_ARQUIVO, "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)

def autenticar_usuario():
    usuarios = carregar_usuarios()
    usuario = input("Digite o nome de usuário: ").strip()
    senha = input("Digite a senha: ").strip()
    senha_hash = gerar_hash(senha)

    if usuario in usuarios and usuarios[usuario] == senha_hash:
        print("Login bem-sucedido!")
        exibir_menu2()
        while True:
            try:
                escolha2 = int(input("Selecione uma disciplina (0 para voltar): "))
                if escolha2 == 0:
                    print("Voltando ao menu principal...")
                    break
                disciplina = selecionar_disciplina(escolha2)
                if disciplina:
                    print(f"Você selecionou: {disciplina}")
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")
    else:
        print("Usuário ou senha incorretos.")

def lista_alunos():
    alunos = carregar_dados(CAMINHO_ARQUIVO)
    if not alunos:
        print("nenhum aluno cadastrado.")
        return
    for idx, aluno in enumerate(alunos, start=1):
        print(f"{idx}. {aluno['nome']} | Idade: {aluno['idade']} |senha: {aluno['senha']}")

# def autenticar_usuario():
#     alunos = carregar_dados(CAMINHO_ARQUIVO)
#     nome = input("Usuário: ").strip().lower()
#     senha = input("Senha: ").strip()

#     if nome in alunos and alunos[nome] == gerar_hash(senha):
#         print(f"Login bem-sucedido. Bem-vindo, {nome}!")
#     else:
#         print("Usuário ou senha incorretos.")
