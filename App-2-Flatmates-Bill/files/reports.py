from fpdf import FPDF
import webbrowser
import os

class PdfReport:
    """"
    Class PdfReport reports in a pdf file the due amount per each flatmate relative to the given period. 
    """

    def __init__(self, filename):
        self.filename = filename

    def save(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        
        pdf.image('house.png', w=100, h=100)

        pdf.set_font(family='Times', size=18, style='B')
        pdf.cell(w=0, h=100, txt='Flatmates Bill', border=0, align='C', ln=1)

        pdf.cell(w=130, h=50, txt="Period:", border=0)
        pdf.cell(w=130, h=50, txt=bill.period, border=0, ln=1)

        
        pdf.set_font(family='Times', size=14)

        pdf.cell(w=130, h=50, txt=flatmate1.name, border=0)
        pdf.cell(w=130, h=50, txt=str(round(flatmate1.pays(bill, flatmate2),2))+" "+bill.currency, border=0, ln=1)

        pdf.cell(w=130, h=50, txt=flatmate2.name, border=0)
        pdf.cell(w=130, h=50, txt=str(round(flatmate2.pays(bill, flatmate1),2))+" "+bill.currency, border=0, ln=1)

        pdf.output(self.filename)
        webbrowser.open('file://'+os.path.realpath(self.filename))