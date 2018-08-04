'''
Author: Prasamsa
Date: 4 august 2018
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    char_input = ''
    for char_input in str_input:
        if char_input in('!', '@', '#', '$', '%', '^', '&', '*'):
            str_input = str_input.replace(char_input, " ")
    print(str_input)

if __name__ == "__main__":
    main()
