'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''read input strings'''
    n_val = int(input())
    l = []
    string_final = ""
    for _ in range(n_val):
        string_input = input()
        l.append(string_input)
    string_final = "".join(l)
    return string_final
        
    #     string_final += "".join((string_input).split("\n"))
    # print(string_final)

if __name__ == '__main__':
    main()
