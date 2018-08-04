'''
Author:Prasamsa
Date:4 august 2018
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num = int(input())
    for i in range(1, num+1):
        if i%3 == 0 and i%5 == 0:
            print("Fizz")
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    main()
