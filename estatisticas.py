from utils import carregar_dados
from statistics import mode, StatisticsError

def estatisticas_sistema():
    alunos = carregar_dados("data/alunos.json")
    professores = carregar_dados("data/professores.json")
    cursos = carregar_dados("data/cursos.json")
    logs = carregar_dados("data/log.json")

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

    tempos = []
    for aluno, dados in logs.items():
        for registro in dados.get("registros", []):
            tempo = registro.get("tempo_em_segundos")
            if tempo is not None:
                tempos.append(tempo)

    if tempos:
        media_segundos = sum(tempos) / len(tempos)
        minutos_media = int(media_segundos // 60)
        segundos_media = int(media_segundos % 60)
        print(f"Média de Tempo na Plataforma: {minutos_media} minutos e {segundos_media} segundos")

        try:
            moda_segundos = mode(tempos)
            minutos_moda = int(moda_segundos // 60)
            segundos_moda = int(moda_segundos % 60)
            print(f"Moda de Tempo na Plataforma: {minutos_moda} minutos e {segundos_moda} segundos")
        except StatisticsError:
            print("Moda de Tempo na Plataforma: Não existe uma moda clara (valores únicos ou multimodais).")
    else:
        print("Média e Moda de Tempo na Plataforma: N/A (nenhum registro encontrado)")
