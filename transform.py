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

TIPOS = {
    'regiao': 'int8', 'uf': 'int8', 'municipio': 'int32', 'secao': 'category',
    'subclasse': 'int32', 'saldo_movimentacao': 'int8', 'cbo': 'int32',
    'categoria': 'int16', 'grau_instrucao': 'int8', 'idade': 'Int8',
    'horas_contratuais': 'float32', 'raca_cor': 'int8', 'sexo': 'int8',
    'tipo_empregador': 'int8', 'tipo_estabelecimento': 'int8',
    'tipo_movimentacao': 'int8', 'tipo_deficiencia': 'int8',
    'ind_trab_intermitente': 'int8', 'ind_trab_parcial': 'int8',
    'salario': 'float64', 'tam_estab_jan': 'int8', 'indicador_aprendiz': 'int8',
    'origem_informacao': 'int8', 'indicador_fora_prazo': 'int8',
    'unidade_salario': 'int8', 'valor_salario_fixo': 'float64',
}
COLUNAS_DATA = ['competencia_mov', 'competencia_dec']
def converter_tipos(bloco):
    for col in COLUNAS_DATA:
        bloco[col] = pd.to_datetime(bloco[col].astype(str), format='%Y%m')
    return bloco.astype(TIPOS)
    