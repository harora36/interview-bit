# Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.

class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, a):
        row = 0
        col = 0
        n = len(a)
        m = len(a[0])
        arr = []
        while row < n and col < m:
            for i in range(col, m):
                arr.append(a[row][i])
            row += 1
            for i in range(row, n):
                arr.append(a[i][m-1])
            m -= 1
            if row < n:
                for i in range(m-1, col-1, -1):
                    arr.append(a[n-1][i])
                n -= 1
            if col < m:
                for i in range(n-1, row-1, -1):
                    arr.append(a[i][col])
                col += 1
        return arr
