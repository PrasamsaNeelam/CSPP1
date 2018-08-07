'''
Author: Prasamsa
Date: 7 august 2018
'''

def is_in(char, a_str):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if char == a_str[0]:
        return True
    elif len(a_str) == 1:
        return False
    return is_in(char, a_str[1: ])


def main():
    '''checks whether char is in the given string'''
    data = input()
    data = data.split()
    print(is_in(data[0], data[1]))


if __name__ == "__main__":
    main()
