'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''read input strings'''
    n_val = int(input())
    for _ in range(n_val):
        string_input = input()
        print(string_input)

if __name__ == '__main__':
    main()
