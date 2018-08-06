'''
Author: Prasamsa
Date: 6 august 2018
'''

def square(x_input):
    '''
    x: int or float.
    '''
    return x_input**2


def fourth_power(x_input):
    '''
    x: int or float.
    '''
    return square(square(x_input))

def main():
    '''enter the value that need to be the fourth power '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(fourth_power(int(float(str(data)))))
    else:
        print(fourth_power(data))

if __name__ == "__main__":
    main()
