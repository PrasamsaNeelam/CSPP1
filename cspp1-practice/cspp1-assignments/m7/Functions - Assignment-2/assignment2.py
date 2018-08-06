'''
Author: Prasamsa
Date: 6 august 2018
'''

def payingdebtoff_inayear(balance, annualinterest_rate):
    '''calculate lowest monthly payment'''
    monthly_interest_rate = annualinterest_rate/12
    monthly_payment = 0
    final_balance = balance
    while final_balance > 0:
        monthly_payment += 10
        final_balance = balance
        month = 1
        while month <= 12 and final_balance > 0:
            final_balance -= monthly_payment
            final_balance += (monthly_interest_rate * final_balance)
            month += 1
    ans = "Lowest Payment: "+ str(monthly_payment)
    print(ans)

def main():
    '''input the value'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    payingdebtoff_inayear(data[0], data[1])

if __name__ == "__main__":
    main()
