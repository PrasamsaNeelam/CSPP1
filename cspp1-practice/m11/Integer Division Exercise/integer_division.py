'''
Author: Prasamsa
Date: 10 august 2018
'''

def integer_division(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count

def main():
    data = input()
    data = data.split()
    print(integer_division(int(data[0]), int(data[1])))


if __name__== "__main__":
    main()