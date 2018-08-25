'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    adictionary = sorted(dictionary)
    dict_keys = dictionary.keys()
    dict_values = dictionary.values()
    freq_count = range(len(dict_keys))
    for i in adictionary:
        print(i,"-","##")


def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
