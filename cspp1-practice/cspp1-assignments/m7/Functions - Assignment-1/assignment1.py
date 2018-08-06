'''
Author: Prasamsa
Date: 6 august 2018
'''

def payingdebtoff_inayear(balance_initial, annual_interestrate, monthly_paymentrate):
    '''calculate remaining balance'''
    balance_final = balance_initial
    iterator = 1
    while iterator <= 12:
        monthly_interestrate = annual_interestrate/12.0
        min_monthly_payment = monthly_paymentrate*balance_final
        monthly_unpaid_bal = balance_final - min_monthly_payment
        balance_final = monthly_unpaid_bal + (monthly_interestrate * monthly_unpaid_bal)
        iterator += 1
    return "Remaining balance: " + str(round(balance_final, 2))

def main():
    '''input the value'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print(payingdebtoff_inayear(data[0], data[1], data[2]))

if __name__ == "__main__":
    main()
