import json
import hashlib
from cryptography.fernet import Fernet
import os

class SegurancaEscola:
    def __init__(self):
        # Inicializa a chave de criptografia, criando se não existir
        self.chave = self._gerar_ou_carregar_chave()
        self.cipher = Fernet(self.chave)
        self.dados_file = "data/alunos.json"  # Caminho do arquivo de dados
        os.makedirs("data", exist_ok=True)    # Garante que a pasta exista

    def _gerar_ou_carregar_chave(self):
        """
        Gera uma nova chave ou carrega uma existente do arquivo.
        Isso garante que os dados criptografados possam ser lidos futuramente.
        """
        key_file = "data/chave.key"
        if os.path.exists(key_file):
            with open(key_file, "rb") as f:
                return f.read()
        key = Fernet.generate_key()
        with open(key_file, "wb") as f:
            f.write(key)
        return key

    def _hash_senha(self, matricula, senha):
        """
        Cria um hash SHA-256 da senha combinada com a matrícula.
        A matrícula age como um "salt" para dificultar ataques de dicionário.
        """
        return hashlib.sha256((matricula + senha).encode()).hexdigest()

    def cadastrar_aluno(self, matricula, senha, dados):
        """
        Cadastra um novo usuário (aluno ou professor).
        - Armazena a senha como hash.
        - Os dados são criptografados com a chave.
        - Verifica se a matrícula já existe.
        """
        registros = self._carregar_dados()
        
        if matricula in registros:
            raise ValueError("Matrícula já cadastrada")
        
        registros[matricula] = {
            "senha_hash": self._hash_senha(matricula, senha),
            "dados": self.cipher.encrypt(json.dumps(dados).encode()).decode(),
            "tipo": dados.get("tipo", "aluno")  # padrão é aluno
        }
        
        self._salvar_dados(registros)

    def verificar_acesso(self, matricula, senha):
        """
        Verifica se a matrícula existe e se a senha está correta.
        """
        registros = self._carregar_dados()
        if matricula not in registros:
            return False
        return registros[matricula]["senha_hash"] == self._hash_senha(matricula, senha)

    def obter_dados(self, matricula):
        """
        Retorna os dados descriptografados de um usuário.
        """
        registros = self._carregar_dados()
        dados_cripto = registros.get(matricula, {}).get("dados", "")
        return json.loads(self.cipher.decrypt(dados_cripto.encode()).decode()) if dados_cripto else {}

    def listar_por_tipo(self, tipo, matricula_admin, senha_admin):
        """
        Lista todos os usuários de um tipo específico, como "aluno" ou "professor".
        Requer login de um professor com nível administrador.
        """
        if not self._verificar_admin(matricula_admin, senha_admin):
            return None
            
        registros = self._carregar_dados()
        return {
            matricula: self.obter_dados(matricula)
            for matricula, info in registros.items()
            if info["tipo"] == tipo
        }

    def _verificar_admin(self, matricula, senha):
        """
        Verifica se o usuário é um professor com permissão de administrador.
        """
        if not self.verificar_acesso(matricula, senha):
            return False
        dados = self.obter_dados(matricula)
        return dados.get("tipo") == "professor" and dados.get("admin", False)

    def _carregar_dados(self):
        """
        Lê os dados do arquivo JSON, ou retorna um dicionário vazio se o arquivo estiver corrompido ou ausente.
        """
        try:
            with open(self.dados_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _salvar_dados(self, dados):
        """
        Salva os dados no arquivo JSON.
        """
        with open(self.dados_file, "w") as f:
            json.dump(dados, f, indent=2)


# Demonstração rápida de como usar a classe
if __name__ == "__main__":
    seg = SegurancaEscola()
    
    # Cadastro inicial, só é feito se o arquivo ainda não existir
    if not os.path.exists(seg.dados_file):
        # Adiciona um professor admin
        seg.cadastrar_aluno(
            "2024PROF01", 
            "admin123",
            {"nome": "Diretor Silva", "tipo": "professor", "admin": True, "disciplinas": ["Matemática"]}
        )
        
        # Adiciona um aluno de exemplo
        seg.cadastrar_aluno(
            "20240001A",
            "aluno123",
            {"nome": "João Santos", "tipo": "aluno", "turma": "3A", "notas": {}}
        )
        print("✅ Cadastros iniciais criados!")
