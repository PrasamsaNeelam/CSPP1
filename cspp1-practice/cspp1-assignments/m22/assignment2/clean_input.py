'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
def clean_string(string):
    '''removes all the special characters and spaces'''
    string = ''.join(e for e in string if e.isalnum())
    return string

def main():
    '''reads input string'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
