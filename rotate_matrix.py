class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        for i in range(0, int(n / 2)):
            for j in range(i, n - i - 1):
                val = A[i][j]
                A[i][j] = A[n - j - 1][i]
                A[n - j - 1][i] = A[n - i - 1][n - j - 1]
                A[n - i - 1][n - j - 1] = A[j][n - i - 1]
                A[j][n - i - 1] = val
        return A
