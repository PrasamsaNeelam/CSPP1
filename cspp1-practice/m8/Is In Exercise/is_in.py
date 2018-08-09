'''
Author:Prasamsa
Date: 7 August 2018
'''
def isin(char, astr):
    '''sorting of a given string'''
    sort_str = sorted(astr)
    boolean = isin_2(0,len(sort_str),char, sort_str)
    return boolean
def isin_2(min_um, max_um, char, astr):
    '''
    char:a single character
    astr:an alphabetical string
    it returns true if char is present in astr otherwise false
    '''
    mid = (min_um + max_um)//2
    if astr[mid] == char:
        return "True"
    elif mid in (min_um, max_um):
        return "False"
    else:
        if astr[mid] > char:
            return isin_2(min_um, mid, char, astr)
        elif astr[mid] < char:
            return isin_2(mid, max_um, char, astr)
def main():
    '''main function'''
    data = input()
    data = data.split()
    print(isin((data[0][0]), data[1]))
if __name__ == "__main__":
    main()
