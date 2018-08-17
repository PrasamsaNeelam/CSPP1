'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    list_one = []
    list_two = []
    lower_case_one = dict1.lower()
    lower_case_two = dict2.lower()
    word_list = lower_case_one.split(" ")
    word_listt = lower_case_two.split(" ")
    for _ in word_list:
        list_one.append(_.strip(".,?'"))
    for _ in word_listt:
        list_two.append(_.strip(".,?'"))
    stop_words = load_stopwords("stopwords.txt")
    stopwords_list = stop_words.keys()
    for i in stopwords_list:
        for j in list_one:
            if i == j:
                list_one.remove(j)
    for i in stopwords_list:
        for j in list_two:
            if i == j:
                list_two.remove(j)
    print(list_one)
    print(list_two)

def freq_count(list_one, list_two):
    a_dict = {}
    for i in list_one:
        for j in list_two:
            if i == j:
                if i in a_dict:
                    a_dict[i].append(j)
                else:
                    a_dict[i] = [j] 



        


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
