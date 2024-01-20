from fpdf import FPDF

def exportar_pdf(self, relatorio):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt=relatorio, ln=True, align='C')
    pdf.output("relatorio.pdf")
