'''
Author: Prasamsa
Date: 7 august 2018
'''

def sum_of_digits(number):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if number == 0:
        return number
    return number%10 + sum_of_digits(number//10)

def main():
    '''to calculate the sum of digits'''
    a_value = input()
    print(sum_of_digits(int(a_value)))

if __name__ == "__main__":
    main()
