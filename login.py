import json
import hashlib
import os
from utils import carregar_dados
from cursos import exibir_menu2,selecionar_disciplina,menu_prof
from seguranca import bloqueio_tentativas
from progresso import registro


CAMINHO_ARQUIVO = 'data/alunos.json'
CAMINHO_PROF = 'data/professores.json'

#instância global
seguranca = bloqueio_tentativas()

def gerar_hash(senha):
    return hashlib.sha256(senha.encode('utf-8')).hexdigest()

def salvar_usuarios(usuarios):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=2, ensure_ascii=False)

def carregar_usuarios():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return {}
    with open(CAMINHO_ARQUIVO, "r") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return {}

def lista_alunos():
    alunos = carregar_dados(CAMINHO_ARQUIVO)
    if not alunos:
        print("nenhum aluno cadastrado.")
        return
    for idx, (nome, dados) in enumerate(alunos.items(), start=1):
        print(f"{idx}. {nome} | ID: {dados.get('id', 'N/A')}")

def autenticar_usuario():
    usuarios = carregar_usuarios()
    usuario = input("Digite o nome de usuário: ").strip()

    pode, tempo_restante = seguranca.pode_tentar(usuario)
    if not pode:
        print(f"Número de tentativas máximo. Tente novamente em {tempo_restante} segundos.")
        return

    senha = input("Digite a senha: ").strip()
    senha_hash = gerar_hash(senha)

    if usuario in usuarios and usuarios[usuario]["senha"] == senha_hash:
        print("Login bem-sucedido!")
        from datetime import datetime
        inicio = datetime.now()
        seguranca.resetar_tentativas(usuario)
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
        fim = datetime.now()
        tempo_total = (fim - inicio).total_seconds()
        registro(usuario, tempo_total)
    else:
        print("Usuário ou senha incorretos.")
        bloqueio = seguranca.registrar_erro(usuario)
        if bloqueio:
            print(f"Número de tentativas máximo. Tente novamente em {tempo_restante} segundos.")

def salvar_professor(professor):
    with open(CAMINHO_PROF, "w") as arquivo:
        json.dump(professor, arquivo, indent=4)

def carregar_professor():
    if not os.path.exists(CAMINHO_PROF):
        return {}
    with open(CAMINHO_PROF, "r") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return {}

def autenticar_professor():
    professores = carregar_professor()
    professor = input("Digite o seu nome: ").strip()
    senha = input("Digite a sua senha: ").strip()
    senha_hash = gerar_hash(senha)
    
    if professor in professores and professores[professor]["senha"] == senha_hash:
        print("Login bem-sucedido!")
        menu_prof()
    else:
        print("Erro no login")

def lista_professores():
    professores = carregar_dados(CAMINHO_PROF)
    if not professores:
        print("nenhum professor cadastrado.")
        return
    for idx, (nome, dados) in enumerate(professores.items(), start=1):
        print(f"{idx}. {nome} | Disciplina: {dados['disciplina']}")
