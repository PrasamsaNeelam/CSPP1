'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    '''prints dictionary keys with its values'''
    for i in sorted(dictionary):
        print("{} - {}".format(i, dictionary[i]))
    # dict_keys = dictionary.keys()
    # dict_values = dictionary.values()
    # for i in dict_keys:
    #     for j in dict_values:
    #     print(str(i)+" - "+str[j])
def main():
    '''reads dictionary input'''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
