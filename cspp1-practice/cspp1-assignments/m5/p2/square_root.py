'''
Author: Prasamsa
Date:4 august 2018
'''

def main():
    '''enter the input value to find the square root'''
    square_input = int(input())
    epsilon = 0.01
    step = 0.1
    guess = 0.0
    while abs(guess**2 - square_input) >= epsilon:
        if guess <= square_input:
            guess += step
        else:
            break
    if abs(guess**2 - square_input) >= epsilon:
        print("Failed to compute square root of the given number")
    else:
        print(guess)

if __name__ == "__main__":
    main()
