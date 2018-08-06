'''
Author: Prasamsa
Date: 6 august 2018
'''


def odd(x_value):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    return x_value%2 != 0

def main():
    '''input the value to find whether it is odd or even'''
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
