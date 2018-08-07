'''
Author: Prasamsa
Date: 7 august 2018
'''


def gcd_recur(a_input, b_input):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b_input > a_input:
        a_input, b_input = b_input, a_input
    if b_input % a_input == 0:
        return a_input
    return gcd_recur(b_input, (a_input%b_input))

def main():
    '''input two values to find GCD by recursion method'''
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
