import pandas as pd
CHUNK = 500_000
RENOMEAR = {
    'competênciamov': 'competencia_mov',
    'região': 'regiao',
    'uf': 'uf',
    'município': 'municipio',
    'seção': 'secao',
    'subclasse': 'subclasse',
    'saldomovimentação': 'saldo_movimentacao',
    'cbo2002ocupação': 'cbo',
    'categoria': 'categoria',
    'graudeinstrução': 'grau_instrucao',
    'idade': 'idade',
    'horascontratuais': 'horas_contratuais',
    'raçacor': 'raca_cor',
    'sexo': 'sexo',
    'tipoempregador': 'tipo_empregador',
    'tipoestabelecimento': 'tipo_estabelecimento',
    'tipomovimentação': 'tipo_movimentacao',
    'tipodedeficiência': 'tipo_deficiencia',
    'indtrabintermitente': 'ind_trab_intermitente',
    'indtrabparcial': 'ind_trab_parcial',
    'salário': 'salario',
    'tamestabjan': 'tam_estab_jan',
    'indicadoraprendiz': 'indicador_aprendiz',
    'origemdainformação': 'origem_informacao',
    'competênciadec': 'competencia_dec',
    'indicadordeforadoprazo': 'indicador_fora_prazo',
    'unidadesaláriocódigo': 'unidade_salario',
    'valorsaláriofixo': 'valor_salario_fixo',
}

def ler_mov(caminho):
    return pd.read_csv(caminho, sep=';', decimal=',', encoding='utf-8', chunksize=CHUNK)

