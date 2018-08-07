'''
Author: Prasamsa
Date: 7 august 2018
'''

def factorial(num_input):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if num_input in (1, 0):
        return 1
    return num_input * factorial(num_input-1)

def main():
    '''input a value to find its factorial'''
    a_value = input()
    print(factorial(int(a_value)))

if __name__ == "__main__":
    main()
