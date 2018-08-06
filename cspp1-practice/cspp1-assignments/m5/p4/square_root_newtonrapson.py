'''
Author: Prasamsa
Date: 6 august 2018
'''

def main():
    '''input a value to find the square root in Newton-Raphson method'''
    square_input = int(input())
    epsilon = 0.01
    guess = square_input/2.0
    while abs(guess**2 - square_input) >= epsilon:
        guess = guess - (((guess**2)- square_input)/(2*guess))
    print(guess)

if __name__ == "__main__":
    main()
