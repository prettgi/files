from fpdf import FPDF
import webbrowser
import os

class Bill:
    """
    Class Bill represents the bill of the flat and includes the following attributes: amount, currency and period.
    """

    def __init__(self, amount, currency, period):
        self.amount = amount
        self.currency = currency
        self.period = period


class Flatmate:        
    """
    Class Flatmate defines the flatmates with their attributes: name, days_in_house. 
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_flatmate):
        weight = self.days_in_house / (self.days_in_house + other_flatmate.days_in_house)
        return bill.amount*weight
        



class PdfReport:
    """"
    Class PdfReport reports in a pdf file the due amount per each flatmate relative to the given period. 
    """

    def __init__(self, filename):
        self.filename = filename

    def save(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

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


bill_to_pay = Bill(amount=100, currency = "euros", period = "December 2023")
flatmate1= Flatmate(name="Fred", days_in_house=23)
flatmate2= Flatmate(name="Sarah", days_in_house=28)

print("%s has to pay %.2f %s" %(flatmate1.name, flatmate1.pays(bill_to_pay, flatmate2), bill_to_pay.currency))
print("%s has to pay %.2f %s" %(flatmate2.name, flatmate2.pays(bill_to_pay, flatmate1), bill_to_pay.currency))

pdf = PdfReport(filename="Flatmate_Bill.pdf")
pdf.save(flatmate1,flatmate2, bill_to_pay)













