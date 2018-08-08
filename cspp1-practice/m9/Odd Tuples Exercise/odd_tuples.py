#Exercise : Odd Tuples
'''
Author: Prasamsa
Date: 8 august 2018
'''


def odd_tuples(a_tup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    return a_tup[::2]

def main():
    '''input a tuple'''
    data = input()
    data = data.split()
    a_tup = ()
    l_len = len(data)
    for j in range(l_len):
        a_tup += (data[j],)
    print(odd_tuples(a_tup))

if __name__ == "__main__":
    main()
