"""A matrix is Toeplitz if every diagonal 
from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz."""

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
         for i in range(len(matrix) - 1):
            for j in range(len(matrix[i]) - 1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
         return True