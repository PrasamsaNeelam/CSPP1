'''
    Document Distance - A detailed description is given in the PDF
'''

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    lower_case = dict1.lower()
    word_list = lower_case.split(" ")
    print(word_list)


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
