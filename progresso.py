import json
import os
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(__file__), "log.json")

def carregar():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

def salvar(logs):
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)

def registro(start_time: datetime, duration_seconds: float, option_chosen: str):
    logs = carregar()
    
    dados = {
        "data": start_time.strftime("%d/%m/%Y"),
        "hora": start_time.strftime("%H:%M:%S"),
        "Tempo_de_Uso": duration_seconds,
        "Conteudo_selecionado": option_chosen
    }

    logs.append(dados)
    salvar(logs)