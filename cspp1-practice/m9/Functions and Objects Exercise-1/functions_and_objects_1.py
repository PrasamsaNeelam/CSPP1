'''
Author: Prasamsa
Date: 8 august 2018
'''
def apply_to_each(list_value, func_type):
    '''input: list values
	   output: abs of list values'''
    l_len = len(list_value)
    for i in range(l_len):
        list_value[i] = func_type(list_value[i])
    return list_value

def main():
    '''input any value to get its abs value'''
    data = input()
    data1 = data.split()
    list1 = []
    for j in data1:
        list1.append(int(j))
    print(apply_to_each(list1, abs))

if __name__ == "__main__":
    main()
