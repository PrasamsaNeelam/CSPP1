'''
Author: Prasamsa
Date: 2 august 2018
'''

def main():
    '''computing vowel count'''
    s_s = input()
    c_c = 0
	# the input string is in s
    for char in s_s:
        if char in ('a', 'e', 'i', 'o', 'u'):
            c_c = c_c + 1
    print(c_c)
if __name__ == "__main__":
    main()
