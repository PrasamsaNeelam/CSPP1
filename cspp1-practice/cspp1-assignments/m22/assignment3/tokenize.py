'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    a_dict = {}
    string = string.split()
    for i in string:
        if i in a_dict:
            a_dict[i] += 1
        else:
            a_dict[i] = 1
    return a_dict
            
def main():
    input_value = int(input())
    for _ in range(input_value):
        string = input()
    result = tokenize(string)

if __name__ == '__main__':
    main()
