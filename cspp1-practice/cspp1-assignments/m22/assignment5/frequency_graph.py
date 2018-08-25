'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    dict_keys = list(dictionary.keys())
    dict_values = list(dictionary.values())
    dict_final = dict_keys[:]
    dict_final.sort()
    for i in dict_final:
        print(i+" "+"-"+" "+str(dict_values[dict_keys.index(i)*"#"]))
    return dict_final

def main():
    dictionary = eval(input())
    print(frequency_graph(dictionary))

if __name__ == '__main__':
    main()
