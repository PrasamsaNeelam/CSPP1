'''
Author: Prasamsa
Date: 7 august 2018
'''

def gcd_iter(a_input, b_input):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    i = 0
    small_num = min(a_input, b_input)
    for i in range(small_num, 0, -1):
        if a_input%i == 0 and b_input%i == 0:
            break
    return i
def main():
    '''enter two values to find the GCD'''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
