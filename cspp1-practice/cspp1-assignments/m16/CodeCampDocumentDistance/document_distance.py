'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    import math
    list_one = []
    list_two = []
    a_numerator = 0
    den_one = 0
    den_two = 0
    a_denominator = 0
    compute_final = 0
    dict1 = dict1.lower()
    dict2 = dict2.lower()
    str_one = ''
    str_two = ''
    for i in dict1:
        if 'a' <= i <='z' or i == ' ':
            str_one += i
    for i in dict2:
        if 'a' <= i <='z' or i == ' ':
            str_two += i
    list_one = str_one.split()
    list_two = str_two.split()
    stop_words = load_stopwords("stopwords.txt")
    stopwords_list = stop_words.keys()
    a_clone = list_one[:]
    for i in a_clone:
        if i in stopwords_list:
            list_one.remove(i)
    a_clone = list_two[:]
    for i in a_clone:
        if i in stopwords_list:
            list_two.remove(i)
    # print(list_one)
    # print(list_two)
    a_dict = freq_count(list_one, list_two)
    #print(a_dict)
    for i in a_dict:
        a_numerator += a_dict[i][0] * a_dict[i][1]
        den_one += a_dict[i][0]**2
        den_two += a_dict[i][1]**2
    # print(a_dict)
    # print(den_one,den_two)
    # print(a_denominator)
    return a_numerator/(math.sqrt(den_one) * math.sqrt(den_two))

def freq_count(list_one, list_two):
    '''Returns the frequency count of two list values'''
    dict_one = {}
    dict_two = {}
    common_dictionary = {}
    for i in list_one:
        if i in dict_one:
            dict_one[i] += 1
        else:
            dict_one[i] = 1
    for i in list_two:
        if i in dict_two:
            dict_two[i] += 1
        else:
            dict_two[i] = 1
    #print(dict_two)
    for i in dict_one:
        if i in dict_two:
            common_dictionary[i] = [dict_one[i], dict_two[i]]
        else:
            common_dictionary[i] = [dict_one[i], 0]
    for i in dict_two:
        if i not in common_dictionary:
            common_dictionary[i] = [0, dict_two[i]]
    return common_dictionary

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
