import json
import os
from datetime import datetime

LOG_FILE = 'data/log.json'

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

def registro(usuario, tempo_total):
    logs = carregar()
    dados = {
        "usuario": usuario,
        "data": datetime.now().strftime("%d/%m/%Y"),
        "hora": datetime.now().strftime("%H:%M:%S"),
        "Tempo_de_Uso": tempo_total
    }
    logs.append(dados)
    salvar(logs)