'''
Author: Prasamsa
Date: 6 august 2018
'''

def main():
    '''input the value to find square root'''
    square_input = int(input())
    epsilon = 0.01
    low_value = 0.0
    high_value = square_input
    ans_value = (high_value + low_value)/2.0
    while abs(ans_value**2 - square_input) >= epsilon:
        if ans_value**2 < square_input:
            low_value = ans_value
        else:
            high_value = ans_value
        ans_value = (high_value + low_value)/2.0
    print(ans_value)

if __name__ == "__main__":
    main()
