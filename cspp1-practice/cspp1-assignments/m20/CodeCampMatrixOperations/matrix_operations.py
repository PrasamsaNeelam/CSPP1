def mult_matrix(matrix_value1, matrix_value2):
    '''
        check if the matrix_value1 columns = matrix_value2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    matrix_result = []
    if len(matrix_value1[0]) != len(matrix_value2):
        print("Error: Matrix shapes invalid for mult")
        return None
    else:
        for i in range(len(matrix_value1)):
            li_st = []
            for j in range(len(matrix_value1)):
                sum_value = 0
                for k in range(len(matrix_value2)):
                    sum_value += (matrix_value1[i][k]*matrix_value2[k][j])
                    li_st.append(sum_value)
            matrix_result.append(li_st)
    return matrix_result

def add_matrix(matrix_value1, matrix_value2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    matrix_result = []
    if len(matrix_value1) != len(matrix_value2):
        print("Error: Matrix shapes invalid for addition")
        return None
    else:
        for i in range(len(matrix_value1)):
            li_st = []
            for j in range(len(matrix_value1[i])):
                li_st.append(matrix_value1[i][j] + matrix_value2[i][j])
            matrix_result.append(li_st)
        return matrix_result

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    
    matrix_value1 = []
    m_val, n_val = input().split(",")
    m_val = int(m_val)
    for i in range(0, m_val):
        matrix_value1.append(list(map(int, input().split())))

    flag = True
    for i in matrix_value1:
        count = 0
        for _ in i:
            count += 1
        if count != len(matrix_value1[0]):
            flag = False
    return matrix_value1, flag

def main():
    '''main function'''
    # read matrix 1
    (matrix_value1, flag1) = read_matrix()
    # read matrix 2
    (matrix_value2, flag2) = read_matrix()
    # add matrix 1 and matrix 2
    if flag1 and flag2:
        print(add_matrix(matrix_value1, matrix_value2))
    # multiply matrix 1 and matrix 2
        print(mult_matrix(matrix_value1, matrix_value2))
    else:
        print("Error: Invalid input for the matrix")

if __name__ == '__main__':
    main()
