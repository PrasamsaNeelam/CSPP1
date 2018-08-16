'''
    Author: Prasamsa
    Date: 14 august 2018
'''

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    sequence = '23456789TJQKA'
    list_one = []
    a_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
              '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    for i in a_dict:
        for j in hand:
            if i == j[0]:
                list_one.append(i[0])
    for i in range(len(sequence) - 4):
        if sequence[i:i+5] == ''.join(list_one):
            return True
    return False

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    card = hand[0][1]
    for i in hand:
        if i[1] != card:
            return False
    return True

def is_four_of_a_kind(hand):
    '''checks for four cards having the same face value'''
    hand_list = [i for i, j in hand]
    set_hand = set(hand_list)
    if len(set_hand) != 2:
        return False
    for i in set_hand:
        if hand_list.count(i) == 4:
            return True
    return False

def is_three_of_a_kind(hand):
    '''returns three cards of same face value'''
    hand_list = [i for i, j in hand]
    set_list = set(hand_list)
    for i in set_list:
        if hand_list.count(i) == 3:
            return True
    return False

def is_two_pair(hand):
    '''returns the two pair cards'''
    hand_list = [i for i, j in hand]
    set_list = set(hand_list)
    two_pairs = [_ for _ in set_list if hand_list.count(_) == 2]
    if len(two_pairs) != 2:
        return False
    return True

def is_one_pair(hand):
    '''returns one pair cards'''
    hand_list = [i for i, j in hand]
    set_list = set(hand_list)
    for i in set_list:
        if hand_list.count(i) == 2:
            return True
    return False

def is_full_house(hand):
    '''returns 3 of a kind and two of a kind cards'''
    if is_three_of_a_kind(hand) and is_one_pair(hand):
        return True
    return False

def is_high_card(hand):
    '''returns no card of a kind'''
    list_one = [] 
    a_dict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,
              '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    hand_list = [i for i, j in hand]
    set_list = set(hand_list)
    if len(set_list) != 5:
        return False
    for i in hand_list:
        for j in a_dict:
            if i == j:
                list_one.append(a_dict[j])
    max_value = max(list_one)
    list_two.append(max_value)
    return(max(list_two))

    
def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''
    if is_straight(hand) and is_flush(hand):
        return 9
    if is_flush(hand):
        return 8
    if is_straight(hand):
        return 7
    if is_four_of_a_kind(hand):
        return 6
    if is_three_of_a_kind(hand):
        return 5
    if is_two_pair(hand):
        return 4
    if is_one_pair(hand):
        return 3
    if is_full_house(hand):
        return 2
    if is_high_card(hand):
        return 1
    return 0
    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush
    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand


def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    list_two = []
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        ha = line.split(" ")
        HANDS.append(ha)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
