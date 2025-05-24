
# 🎓 Sistema de Gestão Acadêmica – PIM UNIP

---

## 📚 Sobre o Projeto

Este sistema foi desenvolvido como **Projeto Integrado Multidisciplinar (PIM)** do **1º semestre** do curso de **Análise e Desenvolvimento de Sistemas** da **UNIP**.  

A aplicação realiza a gestão de alunos, professores e cursos via terminal, utilizando arquivos **JSON** para armazenamento de dados.

---

##  👥 Membros

Este projeto foi desenvolvido pelos alunos da UNIP no 1º semestre de Análise e Desenvolvimento de Sistemas:

-   [**Danilo Cardoso**](https://github.com/HenriTwo)
    
-   [**Fábio Henrique**](https://github.com/FabioHenrique9614)
    
-   [**Guilherme Henrique**](https://github.com/guilhermecunha777)
    
-   [**Leonardo Fischer**](https://github.com/LFischer2)
    
-   [**Lucca Vieira**](https://github.com/luccavsn)
    
-   [**Matheus Gabriel**](https://github.com/matheussteck)

---

## ⚙️ Funcionalidades

- ✅ Cadastro e autenticação de **alunos**  
- ✅ Cadastro, autenticação e **bloqueio temporário** de **professores** após tentativas inválidas  
- ✅ Cadastro e listagem de **cursos**  
- ✅ Registro de logs de uso (data, hora, tempo de sessão, opção escolhida)  
- ✅ Interface **CLI** (Command-Line Interface) com menu interativo  

---

## 🛠 Tecnologias e Bibliotecas

| Tecnologia | Uso no projeto |
|------------|----------------|
| **Python 3.13** | Linguagem principal |
| `json` | Leitura/escrita de dados |
| `hashlib` | Criptografia das senhas com SHA-256 |
| `os` | Limpeza de tela e manipulação de caminhos |
| `time` / `datetime` | Controle de bloqueio e registro de tempo |

Os dados são armazenados localmente em arquivos **`.json`**, não sendo necessário banco de dados externo.

---

## 📁 Estrutura do Projeto

| Arquivo/Módulo | Responsabilidade |
|----------------|------------------|
| `main.py` | Menu principal e fluxo da aplicação |
| `alunos.py` | Cadastro e login de alunos |
| `professores.py` | Cadastro e login de professores |
| `login.py` | Função de login (entrada de alunos e professores |
| `cursos.py`| Função de cursos |
| `seguranca.py`| Funções de segurança |
| `utils.py` | Funções auxiliares: salvar/carregar dados, limpar tela |

---

## ▶️ Como Executar

```bash
git clone https://github.com/guilhermecunha777/projeto-do-pim.git
