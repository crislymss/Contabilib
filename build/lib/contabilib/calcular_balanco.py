def calcularbalanco(ativos, passivos, periodo):
<<<<<<< HEAD
    
    '''Este metodo calcula o balanco patrimonial de uma empresa.
    
    ...
    
    Atributtes: 
    
    ativos: dict
        Dicionario contendo os ativos da empresa.
    passivos: dict
        Dicionario contendo os passivos da empresa.
    periodo: list
        Lista contendo os meses do periodo.
        
    Returns:
    
        patrimonio_liquido: dict
            Dicionario contendo o patrimonio liquido da empresa.
            
    '''
    
    patrimonio_liquido = {}# Inicializando o patrimônio líquido
=======
    # Inicializando o patrimônio líquido
    patrimonio_liquido = {}
>>>>>>> c4d6aaca632d323ab757b5fd7d07d104b02c3d10

    # Para cada mês no período
    for mes in periodo:
        # Calculando o total de ativos e passivos para o mês
        total_ativos = sum(ativos[mes].values())
        total_passivos = sum(passivos[mes].values())

        # Calculando o patrimônio líquido para o mês
        patrimonio_liquido[mes] = total_ativos - total_passivos

    return patrimonio_liquido
<<<<<<< HEAD
=======


'''ativos = {
    'janeiro': {'ativo_circulante': 10000, 'ativo_nao_circulante': 20000},
    'fevereiro': {'ativo_circulante': 15000, 'ativo_nao_circulante': 25000},
    # ...
}

passivos = {
    'janeiro': {'passivo_circulante': 5000, 'passivo_nao_circulante': 15000},
    'fevereiro': {'passivo_circulante': 6000, 'passivo_nao_circulante': 16000},
    # ...
}

periodo = ['janeiro', 'fevereiro', # ... 
]

patrimonio = calcular_balanco(ativos, passivos, periodo)

print(patrimonio)'''
>>>>>>> c4d6aaca632d323ab757b5fd7d07d104b02c3d10
