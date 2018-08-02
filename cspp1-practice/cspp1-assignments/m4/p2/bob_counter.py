'''
Author:Prasamsa
Date:2 august 2018
'''

def main():
    '''count substring'''
    str_one = input()
    c_c = 0
    for i in range(len(str_one)):
        if str_one[i:i+3] == "bob":
            c_c = c_c+1
    print(c_c)

if __name__ == "__main__":
    main()
