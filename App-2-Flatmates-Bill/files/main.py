from flat import Bill, Flatmate
from reports import PdfReport

amount_bill = input('Please introduce the current amount of the bill:\n')
period_bill = input('Please introduce the current reference period for the bill: E.g. March 2022\n')

name1 = input('What is your name?\n')
days_in_house1 = int(input(f"How many days did you spent, {name1}, in the house during the refence period?\n"))

name2 = input('What is your flatmate name?\n')
days_in_house2 = int(input(f"How many days did {name2} spent in the house during the refence period?\n"))


bill_to_pay = Bill(amount=float(amount_bill), currency = "euros", period = period_bill)
flatmate1 = Flatmate(name=name1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print("%s has to pay %.2f %s" %(flatmate1.name, flatmate1.pays(bill_to_pay, flatmate2), bill_to_pay.currency))
print("%s has to pay %.2f %s" %(flatmate2.name, flatmate2.pays(bill_to_pay, flatmate1), bill_to_pay.currency))

pdf = PdfReport(filename=f"{period_bill}.pdf")
pdf.save(flatmate1,flatmate2, bill_to_pay)













