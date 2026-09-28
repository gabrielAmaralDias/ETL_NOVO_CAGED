from config import STAGING
from extract import conectar , escolher_competencia , baixar , extrair


ftp = conectar()

ftp.quit()
ano , meses = escolher_competencia()
for mes in meses:
    baixar(ano,mes)
    extrair(mes)