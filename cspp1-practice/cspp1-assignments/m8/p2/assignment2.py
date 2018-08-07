# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one number and returns the sum of digits of given number.

# This function takes in one number and returns one number.


def sum_of_digits(number):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if number == 0:
    	return number
    return number%10 + sum_of_digits(number//10)
    


def main():
    a = input()
    print(sum_of_digits(int(a)))  

if __name__== "__main__":
    main()

