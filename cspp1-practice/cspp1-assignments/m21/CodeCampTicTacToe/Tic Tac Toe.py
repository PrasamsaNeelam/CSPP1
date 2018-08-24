'''
Author: Prasamsa
Date: 24 august 2018
'''
def is_horizontal(li_st, turn):
	'''checks for horizontal match'''
	count = 0
	for i in range(3):
		for j in range(3):
			if not li_st[i][j] is turn:
			    count += 1
		if count == 0:
			   return True
		count = 0
	return False

def is_vertical(li_st, turn):
    '''checks for vertical match'''
    count = 0
    for i in range(3):
        for j in range(3):
            if not li_st[j][i] is turn:
                count += 1
        if count == 0:
            return True
        count = 0
    return False

def is_diagnol_forward(li_st, turn):
    '''checks for diagnol forward match'''
    count = 0
    for i in range(3):
        if not li_st[i][i] is turn:
            count += 1
    if count == 0:
        return True
    return False

def is_diagnol_backward(li_st, turn):
    '''checks for diagnol backward match'''
    count = 0
    j = 2
    for i in range(3):
        if not li_st[i][j] is turn:
            count += 1
        j -= 1
    if count == 0:
        return True
    return False

def main():
	'''main function'''
	count = 0
	x_count = 0
	o_count = 0
	char_count = 0
	other_count = 0
	first_row = input().split()
	second_row = input().split()
	third_row = input().split()
	li_st = [first_row, second_row, third_row]
	for i in range(3):
	    for j in range(3):
	        if li_st[i][j] == 'x':
	        	x_count += 1
	        elif li_st[i][j] == 'o':
	        	o_count += 1
	        elif li_st[i][j] == '.':
	            char_count += 1
	        else:
	        	other_count += 1
	if other_count != 0:
		print("invalid input")
	    count += 1
	elif x_count > o_count+1 or o_count > x_count+1:
		print("invalid game")
		count +=1
	turn = 'x'
	boolean_x = (is_horizontal(li_st, turn_x)
                 or is_vertical(li_st, turn_x)
                 or is_diagnol_forward(li_st, turn_x)
                 or is_diagnol_backward(li_st, turn_x))
	turn = 'o':
	boolean_o = (is_horizontal(li_st, turn_o)
                 or is_vertical(li_st, turn_o)
                 or is_diagnol_forward(li_st, turn_o)
                 or is_diagnol_backward(li_st, turn_o))
	if boolean_x and boolean_o and count == 0:
        print("invalid game")
        count += 1
    if boolean_x and count == 0:
        print(turn_x)
        count += 1
    if boolean_o and count == 0:
        print(turn_o)
        count += 1
    if count == 0:
        print("Draw")

if __name__ == '__main__':
    main()
