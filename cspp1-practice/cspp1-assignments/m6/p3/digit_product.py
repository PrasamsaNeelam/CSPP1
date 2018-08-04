'''
Author: Prasamsa
Date: 4 august 2018
'''
def main():
    '''
    Read any number from the input, store it in variable intial_num.
    '''
    initial_num = int(input())
    ans_final = initial_num
    rem = 0
    final_product = 1
    if initial_num < 0:
        initial_num = -(initial_num)
    while initial_num > 1:
        rem = initial_num%10
        initial_num = initial_num//10
        final_product = final_product*rem
    if ans_final > 0:
        print(final_product)
    if ans_final < 0:
        print(-final_product)
    if ans_final == 0:
        print(rem)

if __name__ == "__main__":
    main()
