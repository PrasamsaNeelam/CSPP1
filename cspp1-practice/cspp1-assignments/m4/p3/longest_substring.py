'''
Author : Prasamsa
Date : 02 august 2018

'''
def main():
    '''largest alphabetical sequence in given string'''
    s_initial = input()
    s_1 = s_initial[0]
    ma_x = 0
    c_c = 0
    for i in range(len(s_initial)-1):
        if s_initial[i] <= s_initial[i+1]:
            c_c += 1
            s_1 += s_initial[i+1]
        else:
            if ma_x <= c_c:
                ma_x = c_c
                s_2 = s_1
            c_c = 0
            s_1 = s_initial[i+1]
    if c_c > ma_x:
        s_2 = s_1
    print(s_2)


if __name__ == "__main__":
    main()
