# Assignment-3
'''
Author: Prasamsa
Date: 10 august 2018
'''

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    count = 0
    for _ in word:
        if _ in hand:
            count += 1
    if count == len(word) and word in word_list:
        return True
    return False


def main():
    '''main function'''
    word = input()
    n_value = int(input())
    adict = {}
    for _ in range(n_value):
        data = input()
        l_in = data.split()
        adict[l_in[0]] = int(l_in[1])
    l_input = input().split()
    print(is_valid_word(word, adict, l_input))

if __name__ == "__main__":
    main()
