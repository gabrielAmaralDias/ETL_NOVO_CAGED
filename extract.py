from config import FTP_HOST , FTP_BASE , STAGING , TIPOS
from ftplib import FTP
import py7zr


def conectar(ano=None , competencia=None):
        ftp = FTP(FTP_HOST)
        ftp.encoding = 'latin-1'
        ftp.login()
        caminho = FTP_BASE
        if ano:
            caminho += f'/{ano}'
        if competencia:
            caminho += f'/{competencia}'
        ftp.cwd(caminho)
        return ftp



def listar_anos():
    ftp = conectar()
    anos = [a for a in ftp.nlst() if a.isdigit()]
    ftp.quit()
    return sorted(anos)

def listar_meses(ano):
    ftp = conectar()
    ftp.cwd(ano)
    meses = ftp.nlst()
    ftp.quit()
    return sorted(meses)

def escolher_competencia():
    anos = listar_anos()
    print('Anos disponíveis:', anos)
    ano_escolhido = input('Digite o ano que deseja acessar: ').strip()
    
    meses = listar_meses(ano_escolhido)
    print(f'Meses disponíveis em {ano_escolhido}: ', meses)
    escolha = input('Digite os meses separados por vírgula (ex: 202601 , 202602), ou  "todos" para baixar tudo: ').strip()
    
    if escolha.lower() == 'todos':
        return ano_escolhido , meses
    else:
        selecionados = [m.strip() for m in escolha.split(',')]
        invalidos = [m for m in selecionados if m not in meses]
        if invalidos:
            print(f'Aviso: esses meses não existem na pasta e serão ignorados: {invalidos}')
        return ano_escolhido , [m for m in selecionados if m in meses]
def baixar(ano=None,competencia=None):
   pasta = STAGING / competencia
   pasta.mkdir(parents = True ,  exist_ok = True)
   
   ftp = conectar(ano,competencia)
   for tipo in TIPOS :
       nome = f'CAGED{tipo}{competencia}.7z'
       caminho = pasta / nome
       if caminho.exists():
           print(f'Já existe: {nome}')
           continue
       print(f'baixando {nome}')
       with open(caminho,'wb') as f:
           ftp.retrbinary(f'RETR {nome}' , f.write)
   ftp.quit()
def extrair(competencia):
    pasta = STAGING / competencia
    for tipo in TIPOS:  
        nome_base = f'CAGED{tipo}{competencia}'
        arq7z = pasta / f'{nome_base}.7z'
        arqtxt = pasta / f'{nome_base}.txt'
        if arqtxt.exists():
            print(f'Já extraido : {arqtxt.name}')
            continue
        print(f'Extraindo {arq7z.name}...')
        with py7zr.SevenZipFile(arq7z,'r') as z:
            z.extractall(path=pasta)
        arq7z.unlink()