'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    n_val = int(input())
    string_final = ""
    for i in range(n_val):
        string_input = input()
        string_final += "".join(string_input.split("\n"))
    print(string_final)

if __name__ == '__main__':
    main()
