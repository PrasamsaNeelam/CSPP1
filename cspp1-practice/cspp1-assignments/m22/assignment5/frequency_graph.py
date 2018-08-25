'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    import collections
    count = collections.Counter(dictionary.values())
    print(count)

    # import collections
    # dictionary = sorted(dictionary)
    # for i in range(len(dictionary)):
    #     dictionary[i] = collections.Counter(dictionary[i])
    # print(dictionary)
def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
