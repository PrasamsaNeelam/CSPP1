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
        print("Error! Matrix shapes invalid for mult")
    else:
        for i in range(len(matrix_value1)):
            li_st = []
            for j in range(len(matrix_value1[i])):
                li_st.append(matrix_value1[i][j] * matrix_value2[i][j])
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
        print("Error! Matrix shapes invalid for addition")
    else:
        for i in range(len(matrix_value1)):
            li_st = []
            for j in range(len(matrix_value1[i])):
                li_st.append(matrix_value1[i][j] + matrix_value2[i][j])
            matrix_result.append(li_st)
    return matrix_result

def read_matrix(m):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''

def main():
    # read matrix 1
    matrix_value1 = []
    m,n = input().split(",")
    m = int(m)
    for i in range(0, m):
        matrix_value1.append(list(map(int,input().split())))
    #print(matrix_value1)

    # read matrix 2
    matrix_value2 = []
    m,n = input().split(",")
    m = int(m)
    for i in range(0, m):
        matrix_value2.append(list(map(int,input().split())))
    #print(matrix_value2)

    # add matrix 1 and matrix 2
    add_matrix(matrix_value1, matrix_value2)
    # multiply matrix 1 and matrix 2
    mult_matrix(matrix_value1, matrix_value2)

if __name__ == '__main__':
    main()
