'''
Author: Prasamsa
Date: 9 august 2018
'''

def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    string = "abcdefghijklmnopqrstuvwxyz"
    l_list = list(string)
    for char in letters_guessed:
    	if char in l_list:
    		l_list = l_list.remove(char)
    return ''.join(l_list)

def main():
    '''
    Main function for the given program
    '''
    user_input = input()
    user_input = user_input.split()
    data = []
    for char in user_input:
        data.append(char[0])
    print(get_available_letters(data))


if __name__ == "__main__":
    main()
