import json
from statistics import mean, median, mode, multimode, StatisticsError
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

class EstatisticasLog:
    def _init_(self, caminho_arquivo):
        self.caminho = caminho_arquivo
        self.logs = self._carregar_logs()
        self.tempos_sessoes = self._extrair_tempos()

    def _carregar_logs(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Arquivo de log não encontrado.")
            return {}

    def _extrair_tempos(self):
        tempos = []
        for info in self.logs.values():
            tempos.extend(sessao["tempo_em_segundos"] for sessao in info.get("registros", []))
        return tempos

    def exibir_estatisticas_por_usuario(self):
        print("\n=== Estatísticas de Uso por Usuário ===\n")
        for usuario, info in self.logs.items():
            registros = info.get("registros", [])
            tempos = [r["tempo_em_segundos"] for r in registros]
            total = sum(tempos)
            media = total / len(tempos) if tempos else 0

            print(f"Usuário: {usuario}")
            print(f"  - Acessos: {len(tempos)}")
            print(f"  - Tempo total: {total:.2f} segundos")
            print(f"  - Tempo médio: {media:.2f} segundos\n")

    def exibir_estatisticas_gerais(self):
        print("=== Estatísticas Gerais ===")
        total_sessoes = len(self.tempos_sessoes)

        if total_sessoes == 0:
            print("Sem sessões registradas.")
            return

        print(f"Total de sessões: {total_sessoes}")
        print(f"Tempo médio (média): {mean(self.tempos_sessoes):.2f} segundos")
        print(f"Tempo mediano (mediana): {median(self.tempos_sessoes):.2f} segundos")

        try:
            moda = mode(self.tempos_sessoes)
            print(f"Tempo mais comum (moda): {moda:.2f} segundos")
        except StatisticsError:
            modas = multimode(self.tempos_sessoes)
            if len(modas) > 1:
                modas_formatadas = [f"{m:.2f}" for m in modas]
                print(f"Tempos mais comuns (moda): {modas_formatadas}")
            else:
                print("Sem moda definida.")

    def exibir_tudo(self):
        self.exibir_estatisticas_por_usuario()
        self.exibir_estatisticas_gerais()