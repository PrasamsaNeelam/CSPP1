'''
Author: Prasamsa
Date: 8 august 2018
'''
def inc(x_value):
    '''enter x value to increment it by 1'''
    return x_value+1

def apply_to_each(list_value, func_type):
    '''increments the value'''
    l_len = len(list_value)
    for i in range(l_len):
        list_value[i] = func_type(list_value[i])
    return list_value

def main():
    '''input data'''
    data = input()
    data1 = data.split()
    list1 = []
    for j in data1:
        list1.append(int(j))
    print(apply_to_each(list1, inc))

if __name__ == "__main__":
    main()
