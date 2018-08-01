varA= 2
varB= "hello"
if type(varA) is str or type(varB) is str:
	print("string involved")
elif varA>varB:
	print("bigger")
elif varA=varB:
	print("equal")
else varA<varB:
	print("smaller")