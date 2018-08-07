'''
Author: Prasamsa
Date: 7 august 2018
'''

def iter_power(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    result = 1
    while exp > 0:
        result = result*base
        exp -= 1
    return result

def main():
    '''enter values of base and exponent'''
    data = input()
    data = data.split()
    print(iter_power(float(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
