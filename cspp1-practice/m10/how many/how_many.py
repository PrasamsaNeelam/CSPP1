'''
Author: Prasamsa
Date: 9 august 2018
'''

def how_many(a_dict):
    '''
    a_dict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    values = a_dict.values()
    for i in values:
        for _ in i:
            count += 1
    return count

def main():
    '''main function'''
    input_num = input()
    a_dict = {}
    for _ in range(int(input_num)):
        s_in = input()
        l_in = s_in.split()
        if l_in[0][0] not in a_dict:
            a_dict[l_in[0][0]] = [l_in[1]]
        else:
            a_dict[l_in[0][0]].append(l_in[1])
    print(how_many(a_dict))

if __name__ == "__main__":
    main()
