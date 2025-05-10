import json
import hashlib
import os

USUARIOS_ARQUIVO = "alunos.json"

# Utilitários

# def carregar_usuarios():
#     if not os.path.exists(USUARIOS_ARQUIVO):
#         return {}
#     with open(USUARIOS_ARQUIVO, "r") as arquivo:
#         return json.load(arquivo)


# def salvar_usuarios(usuarios):
#     with open(USUARIOS_ARQUIVO, "w") as arquivo:
#         json.dump(usuarios, arquivo, indent=4)


# def gerar_hash(senha):
#     return hashlib.sha256(senha.encode()).hexdigest()

# Funcionalidades


# def cadastrar_usuario():
#     usuarios = carregar_usuarios()
#     nome = input("Novo usuário: ").strip().lower()

#     if nome in usuarios:
#         print("Usuário já existe.")
#         return

#     senha = input("Nova senha: ").strip()
#     usuarios[nome] = gerar_hash(senha)
#     salvar_usuarios(usuarios)
#     print("Usuário cadastrado com sucesso!")


def autenticar_usuario():
    usuarios = carregar_usuarios()
    nome = input("Usuário: ").strip().lower()
    senha = input("Senha: ").strip()

    if nome in usuarios and usuarios[nome] == gerar_hash(senha):
        print(f"Login bem-sucedido. Bem-vindo, {nome}!")
    else:
        print("Usuário ou senha incorretos.")
