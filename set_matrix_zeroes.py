# Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        n = len(A)
        m = len(A[0])
        row = [1 for i in range(n)]
        col = [1 for i in range(m)]
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        for i in range(n):
            for j in range(m):
                if row[i] == 0 or col[j] == 0:
                    A[i][j] = 0
        return A
