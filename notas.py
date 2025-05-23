from login import carregar_usuarios,salvar_usuarios

def add_nota():
    alunos = carregar_usuarios()
    nome = input("digite o nome do aluno para adicionar a nota: ").strip().lower()

    for aluno in alunos:
        if nome in aluno["nome"].lower():
            try:
                nota = float(input(f"digite a nota para {aluno['nome']}: "))
                aluno["notas"].append(nota)
                salvar_usuarios(alunos)
                print("nota adicionada com sucesso!")
                return
            except ValueError:
                print("nota invalida. use números.")
                return
    print("aluno não encontrado.")