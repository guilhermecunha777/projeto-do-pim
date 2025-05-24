from utils import carregar_dados

def estatisticas_sistema():
    alunos = carregar_dados("data/alunos.json")
    professores = carregar_dados("data/professores.json")
    cursos = carregar_dados("data/cursos.json")

    total_alunos = len(alunos)
    total_professores = len(professores)
    total_cursos = len(cursos)

    print("\n=== Estatísticas do Sistema ===")
    print(f"Total de Alunos: {total_alunos}")
    print(f"Total de Professores: {total_professores}")
    print(f"Total de Cursos: {total_cursos}")

    if total_professores > 0:
        media_cursos_por_professor = total_cursos / total_professores
        print(f"Média de Cursos por Professor: {media_cursos_por_professor:.2f}")
    else:
        print("Média de Cursos por Professor: N/A (nenhum professor cadastrado)")
