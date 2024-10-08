def markRow(matrix,n,m,i):
    for j in range(m):
        if matrix[i][j] != 0:
            matrix[i][j] = -1
            
def markCol(matrix,n,m,j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def setMatrixZero(matrix):
    
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if matrix[i][j] == 0:
               markRow(matrix,n,m,i)
               markCol(matrix,n,m,j)
               
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    
    return matrix
    
def setMatrixZeroBetter(matrix):
    
    n = len(matrix)
    m = len(matrix[0])
    
    row = [0]*n
    col = [0]*m
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            
            if matrix[i][j] == 0:
               row[i] = 1
               col[j] = 1
               
               
    for i in range(n):
        for j in range(m):
            if row[i] or col[j]:
                matrix[i][j] = 0
                
    
    return matrix
    
def main():
    matrix=[[1,1,1],[1,0,1],[1,1,1]]
    ans = setMatrixZeroBetter(matrix)
    print(ans)

if __name__ == "__main__":
    main()