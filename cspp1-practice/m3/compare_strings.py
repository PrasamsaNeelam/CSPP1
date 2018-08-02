'''
Author: Prasamsa
Date: 1 august 2018
'''
VARA = 2
VARB = "hello"
if isinstance(VARA) is str or isinstance(VARB) is str:
    print("string involved")
elif VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")