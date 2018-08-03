'''
Author: Prasamsa
Date: 3 august 2018
'''

def main():
    '''secret number'''
    print("Please think of a number between 0 and 100")
    i = 0
    j = 100
    mid = (i+j)//2
    print("Enter 'h' to indicate the guess is too high")
    print("Enter 'l' to indicate the guess is too low")
    print("Enter 'c' to indicate i guessed correctly")
    print("Is your secret number 50?")
    s_s = input()
    while 1:
        if s_s == 'c':
            print("I guessed it correctly.")
            break
        elif s_s == 'h':
            i = mid
        elif s_s == 'l':
            j = mid
        else:
            print("Sorry, I did not understand your input.")
        mid = (i+j)//2
        print("Is your secret number"+str(mid)+"?")
        s_s = input()
    print("Your secret number was: "+str(mid))

if __name__ == "__main__":
    main()
