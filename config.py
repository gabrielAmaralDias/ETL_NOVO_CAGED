from pathlib import Path

# Pasta raiz do projeto, descoberta a partir deste arquivo
RAIZ = Path(__file__).resolve().parent

# Pastas de trabalho
STAGING = RAIZ / "staging"   # temporária: .7z e .txt baixados
SAIDA = RAIZ / "saida"       # camada final consumida pelo BI

# FTP do Ministério do Trabalho
FTP_HOST = "ftp.mtps.gov.br"
FTP_BASE = "pdet/microdados/NOVO CAGED"

# Tipos de arquivo publicados por competência
TIPOS = ["MOV", "FOR", "EXC"]
