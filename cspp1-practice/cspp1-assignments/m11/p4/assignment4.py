#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function. This function allows the user to play out a single hand. First, though, you'll need to implement the helper calculateHandlen function, which can be done in under five lines of code.


def calculate_hand_len(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    cnt_value = 0
    for k in hand:
        values = k.values()
        cnt_value += values
    return cnt_value

def main():
    '''main function'''
    n_value = input()
    adict = {}
    for _ in range(int(n_value)):
        data = input()
        l_in = data.split()
        adict[l_in[0]] = int(l_in[1])
    print(calculate_hand_len(adict))
        


if __name__ == "__main__":
    main()
