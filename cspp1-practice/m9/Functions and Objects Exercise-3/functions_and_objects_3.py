'''
Author: Prasamsa
Date: 8 august 2018
'''

def square(x_value):
    '''enter the x value to find square of the value'''
    return x_value**2

def apply_to_each(list_value, func_type):
    '''input the list and square function'''
    l_len = len(list_value)
    for i in range(l_len):
        list_value[i] = func_type(list_value[i])
    return list_value

def main():
    '''main function'''
    data = input()
    data1 = data.split()
    list1 = []
    for j in data1:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__ == "__main__":
    main()
