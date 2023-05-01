def read_matrix():
    input_num = input("Please input your matrix below:\n")
    matrix = []
    value = []
    while(input_num!=""):
        for i in input_num:
            if(i.isdigit()):
                value.append(int(i))
        matrix.append(value)
        value = []
        input_num = input()
    return(matrix)

def scalar_multiplication(matrix, scalar):
    multiplied_matrix=[]
    for i in matrix:
        value = []
        for j in i:
            k=scalar*j
            if(str(k).find('.')==True):
                value.append(float(k))
            else:
                value.append(int(k))
        multiplied_matrix.append(value)
    return(multiplied_matrix)

def transpose(matrix):
    transpose_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transpose_matrix.append(new_row)
    return(transpose_matrix)

if __name__ == "__main__":
    main_matrix=read_matrix()
    print(f"Your matrix:\n{main_matrix}")
    scalar_matrix=scalar_multiplication(main_matrix,scalar=8)
    print(f"Scalar multiplication with 8:\n{scalar_matrix}")
    transpose_matrix=transpose(main_matrix)
    print(f"Transposition:\n{transpose_matrix}")