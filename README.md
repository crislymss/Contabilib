# Contabilib: Biblioteca Python para Manipulações de Serviços de Contabilidade

O Contabilib é uma biblioteca Python desenvolvida para lidar com tarefas comuns de contabilidade, como cálculo de rescisão, balanço patrimonial, demonstração de resultados e criação de gráficos financeiros. Ele oferece uma ferramenta de ajuda para programadores que desejam integrar esses serviços contábeis em seus projetos.

## Funcionalidades

### Cálculo de Rescisão

- A função `calcular_rescisao()` permite calcular a rescisão de um funcionário com base em variáveis como salário, tempo de serviço, motivos da rescisão, entre outros.

### Balanço Patrimonial

- O Contabilib fornece funções para calcular ativos, passivos e patrimônio líquido da empresa em um determinado período.


### Gráficos Financeiros

- Oferece funcionalidades para criar gráficos visuais de dados financeiros, incluindo gráficos de barras, para uma análise mais intuitiva.

### Exportar para PDF

- A função `exportar_para_pdf()` permite exportar relatórios financeiros para um arquivo PDF, facilitando o compartilhamento e a visualização dos dados.

## Como Usar

1. Instale a biblioteca Contabilib utilizando o pip:

    ```bash
    pip install contabilib
2. Importe a biblioteca em seu projeto Python:
    ```bash
    import contabilib
3. Agora você pode utilizar as funcionalidades oferecidas pela biblioteca Contabilib em seu projeto Python.


## Exemplos

Veja exemplos de como utilizar algumas das funcionalidades da Contabilib:

### Exemplo de Uso: Rescisão Sem Justa Causa

```python
from contabilib import rescisao_sem_justa_causa

salario = 3000
tempo_de_servico = 24

valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais = rescisao_sem_justa_causa(salario, tempo_de_servico)

print("Rescisão sem justa causa:")
print("Valor da rescisão:", valor_rescisao)
print("FGTS:", fgts)
print("Multa FGTS:", multa_fgts)
print("Aviso Prévio:", aviso_previo)
print("Décimo Terceiro:", decimo_terceiro)
print("Férias Proporcionais:", ferias_proporcionais)
```
### Exemplo de Uso: Cálculo de Balanço Patrimonial
```python
from contabilib import calcular_balanco

ativos = {
    'janeiro': {'ativo_circulante': 2, 'ativo_nao_circulante': 3},
    'fevereiro': {'ativo_circulante': 15000, 'ativo_nao_circulante': 25000},
}

passivos = {
    'janeiro': {'passivo_circulante': 5000, 'passivo_nao_circulante': 15000},
    'fevereiro': {'passivo_circulante': 6000, 'passivo_nao_circulante': 16000},
}

periodo = ['janeiro', 'fevereiro']

patrimonio = calcular_balanco(ativos, passivos, periodo)

print("Balanço Patrimonial:", patrimonio)
```
### Exemplo de Uso: Gerar PDF Balanço

```python
from contabilib import gerar_pdf_balanco


ativos = {
    'janeiro': {'ativo_circulante': 20000, 'ativo_nao_circulante': 30000},
    'fevereiro': {'ativo_circulante': 25000, 'ativo_nao_circulante': 35000},

}


passivos = {
    'janeiro': {'passivo_circulante': 10000, 'passivo_nao_circulante': 20000},
    'fevereiro': {'passivo_circulante': 12000, 'passivo_nao_circulante': 22000},

}


periodo = ['janeiro', 'fevereiro', conforme necessário
]

gerar_pdf_balanco(ativos, passivos, periodo)
```

### Exemplo de Uso: Gerar PDF Rescisao Sem justa Causa

```python
from contabilib import gerar_pdf_rescisao

valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais = rescisao_sem_justa_causa(
    2000, 12)

nome = "Raimundo Sousa"
cpf = "078.345.213-00"
razaosocial = "Magazine Luiza S/A"
cnpj = "47.960.950/0001-21"
salario = 2000
tempodeservico = 12
causadoafastamento = "Baixo Desempenho do Colaborador"
diadarescisao = "30/01/2024"


gerar_pdf_rescisao(nome, cpf, razaosocial, cnpj, tempodeservico, salario, causadoafastamento,
                   multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais, diadarescisao, valor_rescisao)

```


### Exemplo de Uso: Gerar gráfico Patrimonio e Rescisão
```python
from contabilib import gerargraficorescisao, gerargraficopatrimonio

multafgts = 5000
avisoprevio = 3000
decimoterceiro = 4000
ferias_proporcionais = 2000
valor_rescisao = multafgts + avisoprevio + decimoterceiro + ferias_proporcionais

gerargraficorescisao(multafgts, avisoprevio, decimoterceiro, ferias_proporcionais, valor_rescisao)

patrimonio_liquido = {
    'janeiro': 10000,
    'fevereiro': 12000,
    'março': 15000,
    'abril': 18000,
    'maio': 20000
}

gerargraficopatrimonio(patrimonio_liquido)
```


## Contato

Se você tiver alguma dúvida, sugestão ou se quiser colaborar com o projeto, sinta-se à vontade para entrar em contato com qualquer um dos colaboradores:

### Colaborador 1
- Nome: Crisly Maria
- Email: crisly.santos@ufpi.edu.br

### Colaborador 2
- Nome: Erik Lustosa
- Email: erik.silva@ufpi.edu.br


## Licença

MIT License

Copyright (c) [2024] 
É concedida permissão, gratuitamente, a qualquer pessoa que obtenha uma cópia
deste software e dos arquivos de documentação associados (o "Software"), para lidar
no Software sem restrição, incluindo, sem limitação, os direitos
para usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender
cópias do Software, e permitir que as pessoas a quem o Software é
fornecido o façam, sujeito às seguintes condições:

O aviso de copyright acima e este aviso de permissão devem ser incluídos em todas
cópias ou partes substanciais do Software.





