#1572. Matrix Diagonal Sum

from typing import List
def diagonalSum(mat: List[List[int]]) -> int:
        n = len(mat)
        s= 0
        for i in range(n):
            s += mat[i][i]
            s+= mat[i][n-i-1]
        if n%2 == 1:
            s-= mat[n//2][n//2]
        return s
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))

#498. Diagonal Traverse