REGIAO = {
    1:'Norte', 2:'Nordeste', 3:'Sudeste',4:'Sul',5:'Centro-Oeste',9:'Não Identificado',99:'Não Identificado'
}
UF = {
    11:'Rondônia',12:'Acre',13:'Amazonas',14:'Roraima',15:'Pará',
    16:'Amapá',17:'Tocantins',21:'Maranhão',22:'Piauí',23:'Ceará',
    24:'Rio Grande do Norte',25:'Paraíba',26:'Pernambuco',27:'Alagoas',
    28:'Sergipe',29:'Bahia',31:'Minas Gerais',32:'Espírito Santo',
    33:'Rio de Janeiro',35:'São Paulo',41:'Paraná',42:'Santa Catarina',
    43:'Rio Grande do Sul' , 50:'Mato Grosso do Sul', 51:'Mato Grosso',
    52:'Goiás',53:'Distrito Federal', 99:'Não identificado',
}

GRAU_INSTRUCAO = {
    1:'Analfabeto',2:'Até 5ª Incompleto',3:'5ª Completo Fundamental',
    4: '6ª a 9ª Fundamental', 5: 'Fundamental Completo', 6: 'Médio Incompleto',
    7: 'Médio Completo', 8: 'Superior Incompleto', 9: 'Superior Completo',
    10: 'Mestrado', 11: 'Doutorado', 80: 'Pós-Graduação completa',
    99: 'Não Identificado',
}

RACA_COR = {
    1: 'Branca', 2: 'Preta', 3: 'Parda', 4: 'Amarela', 5: 'Indígena',
    6: 'Não informada', 9: 'Não Identificado',
}

SEXO = {
    1: 'Homem', 3: 'Mulher', 9: 'Não Identificado',
}

TIPO_EMPREGADOR = {
    0: 'CNPJ Raiz', 2: 'CPF', 9: 'Não Identificado',
}

TIPO_ESTABELECIMENTO = {
    1: 'CNPJ', 3: 'CAEPF', 4: 'CNO', 5: 'CEI (CAGED)', 9: 'Não Identificado',
}

TIPO_MOVIMENTACAO = {
    10: 'Admissão por primeiro emprego', 20: 'Admissão por reemprego',
    25: 'Admissão por contrato trabalho prazo determinado',
    31: 'Desligamento por demissão sem justa causa',
    32: 'Desligamento por demissão com justa causa',
    33: 'Culpa Recíproca', 35: 'Admissão por reintegração',
    40: 'Desligamento a pedido',
    43: 'Término contrato trabalho prazo determinado',
    45: 'Desligamento por Término de contrato',
    50: 'Desligamento por aposentadoria', 60: 'Desligamento por morte',
    70: 'Admissão por transferência', 80: 'Desligamento por transferência',
    90: 'Desligamento por Acordo entre empregado e empregador',
    97: 'Admissão de Tipo Ignorado', 98: 'Desligamento de Tipo Ignorado',
    99: 'Não Identificado',
}

TIPO_DEFICIENCIA = {
    0: 'Não Deficiente', 1: 'Física', 2: 'Auditiva', 3: 'Visual',
    4: 'Intelectual (Mental)', 5: 'Múltipla', 6: 'Reabilitado',
    9: 'Não Identificado',
}

SIM_NAO = {  # usado em indtrabintermitente, indtrabparcial, indicadoraprendiz
    0: 'Não', 1: 'Sim', 9: 'Não Identificado',
}

TAM_ESTAB_JAN = {
    1: 'Zero', 2: 'De 1 a 4', 3: 'De 5 a 9', 4: 'De 10 a 19',
    5: 'De 20 a 49', 6: 'De 50 a 99', 7: 'De 100 a 249', 8: 'De 250 a 499',
    9: 'De 500 a 999', 10: '1000 ou Mais', 99: 'Ignorado', 98: 'Inválido',
    97: 'Não se Aplica', 90: 'Não Informado',
}

ORIGEM_INFORMACAO = {
    1: 'eSocial', 2: 'CAGED', 3: 'EmpregadoWEB',
}

SIM_NAO_EXCLUSAO = {  # indicadordeexclusão, indicadordeforadoprazo (só 0/1)
    0: 'Não', 1: 'Sim',
}

UNIDADE_SALARIO = {
    1: 'Hora', 2: 'Dia', 3: 'Semana', 4: 'Quinzena', 5: 'Mês', 6: 'Tarefa',
    7: 'Variável', 99: 'Não Identificado',
}

CATEGORIA = {
    101: 'Empregado - Geral, inclusive público CLT',
    102: 'Empregado - Trabalhador rural pequeno prazo (Lei 11.718/2008)',
    103: 'Empregado - Aprendiz',
    104: 'Empregado - Doméstico',
    105: 'Empregado - Contrato a termo (Lei 9.601/1998)',
    106: 'Trabalhador temporário (Lei 6.019/1974)',
    107: 'Empregado - Verde e Amarelo sem antecipação FGTS',
    108: 'Empregado - Verde e Amarelo com antecipação FGTS',
    111: 'Empregado - Contrato de trabalho intermitente',
    999: 'Não Identificado',
}
SECAO = {
    'A': 'Agricultura, Pecuária, Produção Florestal, Pesca e Aquicultura',
    'B': 'Indústrias Extrativas',
    'C': 'Indústrias de Transformação',
    'D': 'Eletricidade e Gás',
    'E': 'Água, Esgoto, Atividades de Gestão de Resíduos e Descontaminação',
    'F': 'Construção',
    'G': 'Comércio, Reparação de Veículos Automotores e Motocicletas',
    'H': 'Transporte, Armazenagem e Correio',
    'I': 'Alojamento e Alimentação',
    'J': 'Informação e Comunicação',
    'K': 'Atividades Financeiras, de Seguros e Serviços Relacionados',
    'L': 'Atividades Imobiliárias',
    'M': 'Atividades Profissionais, Científicas e Técnicas',
    'N': 'Atividades Administrativas e Serviços Complementares',
    'O': 'Administração Pública, Defesa e Seguridade Social',
    'P': 'Educação',
    'Q': 'Saúde Humana e Serviços Sociais',
    'R': 'Artes, Cultura, Esporte e Recreação',
    'S': 'Outras Atividades de Serviços',
    'T': 'Serviços Domésticos',
    'U': 'Organismos Internacionais e Outras Instituições Extraterritoriais',
    'Z': 'Não identificado',
}