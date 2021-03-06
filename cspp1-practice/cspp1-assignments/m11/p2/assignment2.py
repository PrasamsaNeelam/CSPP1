'''
Author: Prasamsa
Date: 10 august 2018
'''

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    for k in word:
        if k in hand:
            hand[k] -= 1
    return hand


def main():
    '''main function'''
    n_value = input()
    adict = {}
    for _ in range(int(n_value)):
        data = input()
        l_in = data.split()
        adict[l_in[0]] = int(l_in[1])
    data1 = input()
    print(update_hand(adict, data1))


if __name__ == "__main__":
    main()
