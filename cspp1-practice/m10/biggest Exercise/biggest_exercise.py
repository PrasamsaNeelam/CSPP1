'''
Author: Prasamsa
Date: 9 august 2018
'''

def biggest(a_dict):
    '''
    a_dict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    temp_variable = 0
    for k in a_dict:
        count_value = 0
        values = a_dict[k]
        count_value = len(values)
        if temp_variable <= count_value:
            temp_variable = count_value
            st_r = k
    return st_r

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
    print(biggest(a_dict))
if __name__ == "__main__":
    main()
