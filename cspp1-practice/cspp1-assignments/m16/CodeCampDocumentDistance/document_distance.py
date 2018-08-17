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
        list_one.append(_.strip('.,?'))
    for _ in word_listt:
        list_two.append(_.strip('.,?'))
    for i in load_stopwords(file):
        for j in word_list:
            if stopwords[i] == j:
                del j 
   


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
