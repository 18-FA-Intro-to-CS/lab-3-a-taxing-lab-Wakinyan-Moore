'''
payroll.py
A program to calculate taxes and net pay for a given gross pay input
'''

def round_money(amount):
    pennies = round(amount * 100)
    return pennies / 100

def calculate(gross_pay, fed_tax_rate, state_tax_rate):
    '''
    This function takes three parameters and outputs the results of calculating
    net pay. It prints the results of these calculations.
  
    You can assume that all input is correct (there is not user error)
    '''
    # Put your code here.
    pass # Delete this line

def main():
    fed_tax_rate = float(input("Federal tax rate > "))
    state_tax_rate = float(input("state tax rate > "))
    print()
    gross_pay = float(input("Gross Pay > "))
    calculate(gross_pay, fed_tax_rate, state_tax_rate)

main()
