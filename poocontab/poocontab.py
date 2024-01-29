import seaborn as sns
import matplotlib.pyplot as plt
from fpdf import FPDF
def calcularbalanco(ativos, passivos, periodo):
    
    # Inicializando o patrimônio líquido
    patrimonio_liquido = {}

    # Para cada mês no período
    for mes in periodo:
        # Calculando o total de ativos e passivos para o mês
        total_ativos = sum(ativos[mes].values())
        total_passivos = sum(passivos[mes].values())

        # Calculando o patrimônio líquido para o mês
        patrimonio_liquido[mes] = total_ativos - total_passivos

    return patrimonio_liquido


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
multa_fgts = 0
aviso_previo = 0
decimo_terceiro = 0
ferias_proporcionais = 0


def rescisao_sem_justa_causa(salario, tempo_de_servico):

    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    # multa do FGTS é de 40% do saldo do FGTS
    multa_fgts = fgts * 0.4

    # aviso prévio indenizado é um salário
    aviso_previo = salario

    # decimo terceiro salário proporcional
    decimo_terceiro = (salario / 12) * tempo_de_servico

    # ferias proporcionais
    ferias_proporcionais = (salario / 12) * tempo_de_servico

    valor_rescisao = fgts + multa_fgts + aviso_previo + \
        decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_justa_causa(salario, tempo_de_servico):

    # no caso de justa causa, o funcionário não tem direito a multa do FGTS, aviso prévio e décimo terceiro

    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    valor_rescisao = fgts
    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_aposentadoria(salario, tempo_de_servico):
    # Inicializando as variáveis

    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    # no caso de aposentadoria, o funcionário tem direito ao FGTS, mas não à multa do FGTS
    # aviso prévio e décimo terceiro são calculados normalmente
    aviso_previo = salario
    decimo_terceiro = (salario / 12) * tempo_de_servico
    ferias_proporcionais = (salario / 12) * tempo_de_servico

    valor_rescisao = fgts + aviso_previo + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_falecimento(salario, tempo_de_servico):

    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    # no caso de falecimento, os dependentes têm direito ao FGTS, sem multa
    # aviso prévio, décimo terceiro e férias são calculados normalmente
    aviso_previo = salario
    decimo_terceiro = (salario / 12) * tempo_de_servico
    ferias_proporcionais = (salario / 12) * tempo_de_servico

    valor_rescisao = fgts + aviso_previo + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_demissao(salario, tempo_de_servico):

    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    # no caso de pedido de demissão, o funcionário não tem direito a multa do FGTS nem aviso prévio indenizado
    # décimo terceiro e férias são calculados normalmente
    decimo_terceiro = (salario / 12) * tempo_de_servico
    ferias_proporcionais = (salario / 12) * tempo_de_servico

    valor_rescisao = fgts + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


def rescisao_termino_de_contrato_por_experiencia(salario, tempo_de_servico):
    # calculo do FGTS
    fgts = salario * 0.08 * tempo_de_servico

    # no caso de término de contrato de experiência, o funcionário não tem direito a multa do FGTS nem aviso prévio indenizado
    # décimo terceiro e férias são calculados normalmente
    decimo_terceiro = (salario / 12) * tempo_de_servico
    ferias_proporcionais = (salario / 12) * tempo_de_servico

    valor_rescisao = fgts + decimo_terceiro + ferias_proporcionais

    return valor_rescisao, fgts, multa_fgts, aviso_previo, decimo_terceiro, ferias_proporcionais


class PDF_Rescisao(FPDF):
    def header(self):
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, 'TERMO DE RESCISÃO DO CONTRATO DE TRABALHO', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')


def create_pdf(file_name, data):
    pdf = PDF_Rescisao()
    pdf.add_page()

    pdf.set_fill_color(200, 200, 200)  # Cinza claro
    th = 10
    pdf.set_font('Times', '', 14)

    for i, row in enumerate(data):
        if i % 2 == 0:
            pdf.set_fill_color(200, 200, 200)  # Cinza claro para linhas pares
        else:
            pdf.set_fill_color(255, 255, 255)  # Branco para linhas ímpares
        pdf.cell(90, th, str(row[0]), border=1, ln=0, fill=True)
        pdf.cell(0, th, str(row[1]), border=1, ln=1, fill=True)

    pdf.ln(10)

    pdf.cell(0, th, 'Assinatura do Funcionário: ________________________', 0, 1)
    pdf.cell(0, th, 'Assinatura do Empregador: ________________________', 0, 1)

    pdf.output(file_name)


def gerar_pdf_rescisao(nome, cpf, razaosocial, cnpj, tempodeservico, salario, causadoafastamento, multafgts, avisoprevio, decimoterceiro,
                       ferias_proporcionais, diadarescisao, valor_rescisao):

    data = [
        ['Nome do Funcionário', nome],
        ['CPF', cpf],
        ['Razão Social da Empresa', razaosocial],
        ['CNPJ', cnpj],
        ['Tempo de Serviço', tempodeservico],
        ['Dia da Rescisão', diadarescisao],
        ['Causa do Afastamento', causadoafastamento],
        ['Salário', 'R$ ' + salario],
        ['Multa FGTS', 'R$ ' + multafgts],
        ['Aviso Prévio', 'R$ ' + avisoprevio],
        ['Décimo Terceiro', 'R$ ' + decimoterceiro],
        ['Férias Proporcionais', 'R$ ' + ferias_proporcionais],
        ['Valor da Rescisão', 'R$ ' + valor_rescisao],
        # adicione mais campos conforme necessário
    ]

    create_pdf("termo_de_rescisao.pdf", data)


class PDF_Balanco(FPDF):
    def header(self):
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, 'BALANÇO PATRIMONIAL', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')


def create_pdf(file_name, data):
    pdf = PDF_Balanco()
    pdf.add_page()

    pdf.set_fill_color(200, 200, 200)  # Cinza claro
    th = 10
    pdf.set_font('Times', '', 14)

    for i, row in enumerate(data):
        if i % 2 == 0:
            pdf.set_fill_color(200, 200, 200)  # Cinza claro para linhas pares
        else:
            pdf.set_fill_color(255, 255, 255)  # Branco para linhas ímpares
        pdf.cell(90, th, str(row[0]), border=1, ln=0, fill=True)
        pdf.cell(0, th, str(row[1]), border=1, ln=1, fill=True)

    pdf.output(file_name)


def gerar_pdf_balanco(ativos, passivos, periodo):
    data = []
    patrimonio_liquido_total = 0
    for mes in periodo:
        ativo_circulante = ativos[mes]['ativo_circulante']
        ativo_nao_circulante = ativos[mes]['ativo_nao_circulante']
        passivo_circulante = passivos[mes]['passivo_circulante']
        passivo_nao_circulante = passivos[mes]['passivo_nao_circulante']
        patrimonio_liquido = ativo_circulante + ativo_nao_circulante - \
            passivo_circulante - passivo_nao_circulante
        patrimonio_liquido_total += patrimonio_liquido

        data.append([f"Ativo Circulante ({mes})", f"R$ {ativo_circulante}"])
        data.append(
            [f"Ativo Não Circulante ({mes})", f"R$ {ativo_nao_circulante}"])
        data.append(
            [f"Passivo Circulante ({mes})", f"R$ {passivo_circulante}"])
        data.append(
            [f"Passivo Não Circulante ({mes})", f"R$ {passivo_nao_circulante}"])
        data.append(
            [f"Patrimônio Líquido ({mes})", f"R$ {patrimonio_liquido}"])
        data.append(["", ""])  # linha em branco entre os meses

    data.append(["Patrimônio Líquido Total", f"R$ {patrimonio_liquido_total}"])

    create_pdf("balanco_patrimonial.pdf", data)


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

gerar_pdf_balanco(ativos, passivos, periodo)'''


multafgts = 100
avisoprevio = 200
decimoterceiro = 10
ferias_proporcionais = 300
valor_rescisao = 20


def gerargraficorescisao(multafgts, avisoprevio, decimoterceiro, ferias_proporcionais, valor_rescisao):
    # Cria uma lista com os nomes dos componentes da rescisão
    componentes = ['Multa FGTS', 'Aviso Prévio',
                   'Décimo Terceiro', 'Férias Proporcionais', 'Valor Rescisão']

    # Cria uma lista com os valores correspondentes
    valores = [multafgts, avisoprevio, decimoterceiro,
               ferias_proporcionais, valor_rescisao]

    # Define o estilo do gráfico usando seaborn
    sns.set(style="whitegrid")

    # Cria uma figura e um conjunto de subtramas
    fig, ax = plt.subplots()

    # Cria o gráfico de barras
    ax = sns.barplot(x=componentes, y=valores, palette="viridis")

    # Adiciona rótulos e título
    ax.set_title('Valores da Rescisão')
    ax.set_xlabel('Componentes')
    ax.set_ylabel('Valores')

    # Rotaciona os rótulos do eixo x para evitar sobreposição
    plt.xticks(rotation=45)

    # Ajusta a largura das barras para evitar sobreposição
    plt.tight_layout()

    # Salva a figura como uma imagem
    fig.savefig('rescisao.png')

    # Fecha a figura
    plt.close(fig)
