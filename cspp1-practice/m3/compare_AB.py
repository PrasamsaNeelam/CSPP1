VARA = 2
VARB = "hello"
if type(VARA) is str or type(VARB) is str:
    print("string involved")
elif VARA > VARB:
    print("bigger")
elif VARA == VARB:
    print("equal")
else:
    print("smaller")
