'''from fpdf import FPDF

def gerar_pdf_rescisao(dados):
    pdf = FPDF()

    # Adicionando uma página
    pdf.add_page()

    # Definindo a fonte
    pdf.set_font("Arial", size = 12)

    # Adicionando um título
    pdf.cell(0, 10, txt = "CÁLCULO DA RESCISÃO", ln = True, align = 'C')

    # Adicionando os dados
    for chave, valor in dados.items():
        pdf.cell(0, 10, txt = f"{chave}: {valor}", ln = True)

    # Salvando o PDF
    pdf.output("rescisao.pdf")



dados = {
    'DATA ADMISSÃO': '01/01/2021',
    'DATA SAÍDA': '18/03/2022',
    'AVISO PRÉVIO': 'R$ 500,00',
    'SALÁRIO': 'R$ 2.000,00',
    'SALDO DE SALÁRIO': 'R$ 1.133,33',
    'FÉRIAS VENCIDAS': 'R$ 2.000,00',
    'FÉRIAS PROPORCIONAL (12 AVOS)': 'R$ 500,00',
    'FÉRIAS 1/3': 'R$ 833,33',
    '13º PROPORCIONAL': 'R$ 500,00',
    'TOTAL BRUTO': 'R$ 4.966,67'
}



gerar_pdf_rescisao(dados)'''
'''import PyPDF2

def preencher_pdf(template_path, output_path, **dados):
    with open(template_path, 'rb') as template_file:
        pdf_reader = PyPDF2.PdfReader(template_file)
        pdf_writer = PyPDF2.PdfWriter()

        # Itera sobre todas as páginas do PDF
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]

            # Preenche os campos do formulário com os dados fornecidos
            if '/Annots' in page:
                for annot_indirect in page['/Annots']:
                    annot = annot_indirect.get_object()  # Linha corrigida
                    if '/T' in annot and annot['/T'] in dados:
                        annot.update({
                            PyPDF2.generic.NameObject("/V"): PyPDF2.generic.createStringObject(dados[annot['/T']])
                        })

            # Adiciona a página ao novo PDF
            pdf_writer.add_page(page)

        # Salva o novo PDF
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# Exemplo de uso:
dados_para_preencher = {
    "Empregador:": "123456789",

    # Adicione os outros dados aqui...
}
template_path = "C:\\Users\\erikl\\OneDrive\\Área de Trabalho\\UNIVERSIDADE ERIK\\4º PERIODO\\POO II\\PROJETO FINAL\\biblioteca-contablib\\contablib\\modelo_recisao3.pdf"
output_path = "C:\\Users\\erikl\\OneDrive\\Área de Trabalho\\UNIVERSIDADE ERIK\\4º PERIODO\\POO II\\PROJETO FINAL\\biblioteca-contablib\\contablib\\recisao_preenchida.pdf"

preencher_pdf(template_path, output_path, **dados_para_preencher)'''



import requests
from reportlab.pdfgen import canvas

def buscar_cnpj(cnpj):
    # Faz a requisição para a API que retorna as informações do CNPJ
    response = requests.get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}')

    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        return response.json()
    else:
        return None

def salvar_comprovante(cnpj):
    # Busca as informações do CNPJ
    info = buscar_cnpj(cnpj)

    if info is not None:
        # Cria um novo arquivo PDF
        c = canvas.Canvas(f'{cnpj}.pdf')

        # Adiciona as informações do CNPJ ao PDF
        c.drawString(100, 750, f'CNPJ: {info["cnpj"]}')
        c.drawString(100, 730, f'Nome: {info["nome"]}')
        c.drawString(100, 710, f'Situação: {info["situacao"]}')
        # Adicione aqui as outras informações que você deseja incluir no PDF...

        # Salva o PDF
        c.save()
    else:
        print(f'Não foi possível buscar as informações do CNPJ {cnpj}.')

# Exemplo de uso:
salvar_comprovante('47960950000121')


