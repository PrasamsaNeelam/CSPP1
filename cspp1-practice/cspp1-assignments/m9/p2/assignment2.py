'''
Author: Prasamsa
Date: 8 august 2018
'''
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secret_word have been guessed so far.
    '''
    string_value = ""
    for char in secret_word:
    	if char in letters_guessed:
    		string_value = string_value + char
    	else:
    		string_value = string_value + "_"
    return string_value


def main():
    '''
    Main function for current assignment
    '''
    user_input = input()
    if user_input:
        data = user_input.split()
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(get_guessed_word(secret_word, list1))

if __name__ == "__main__":
    main()
