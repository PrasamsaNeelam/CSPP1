'''
Author:Prasamsa
Date: 6 august 2018
'''

def square(x_input):
    '''to find the square of the given number'''
    return x_input**2

def main():
    '''input a value to find the square of the given number'''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))

if __name__ == "__main__":
    main()
