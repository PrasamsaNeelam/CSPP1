'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''read input strings'''
    n_val = int(input())
    string_final = ""
    for _ in range(n_val):
        string_input = input()
        string_final += "".join((string_input).split("\n"))
    print(string_final)

if __name__ == '__main__':
    main()