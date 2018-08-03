'''
Author: Prasamsa
Date: 3 august 2018
'''

def main():
    '''perfect cube'''
    initial_num = int(input())
    i = 0
    while i**3 < initial_num:
        i = i+1
    if i**3 == initial_num:
        print(str(initial_num)+" is a perfect cube")
    else:
        print(str(initial_num)+" is not a perfect cube")

if __name__ == "__main__":
    main()
