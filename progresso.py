def registro(usuario, inicio, fim):
    from datetime import datetime
    import json
    import os

    CAMINHO_LOG = "data/log.json"

    def carregar_logs():
        if os.path.exists(CAMINHO_LOG):
            with open(CAMINHO_LOG, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return {}
        return {}

    def salvar_logs(logs):
        with open(CAMINHO_LOG, "w", encoding="utf-8") as f:
            json.dump(logs, f, ensure_ascii=False, indent=2)

    tempo_total = (fim - inicio).total_seconds()
    logs = carregar_logs()  # Isso precisa ser um DICIONÁRIO

    if not isinstance(logs, dict):
        logs = {}

    if usuario not in logs:
        logs[usuario] = {
            "entradas": 0,
            "registros": []
        }

    logs[usuario]["entradas"] += 1
    logs[usuario]["registros"].append({
        "entrada": inicio.strftime("%d/%m/%Y %H:%M:%S"),
        "saida": fim.strftime("%d/%m/%Y %H:%M:%S"),
        "tempo_em_segundos": tempo_total
    })

    salvar_logs(logs)