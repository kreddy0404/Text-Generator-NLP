income = int(input())
tax_percent = 0

if income <= 15527:
    tax_percent = 0
elif income <= 42707:
    tax_percent = 15
elif income <= 132406:
    tax_percent = 25
else:
    tax_percent = 28

cal_tax = income * tax_percent / 100
print(f'The tax for {income} is {tax_percent}%. That is {cal_tax:.0f} dollars!')
