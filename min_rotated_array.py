# Suppose a sorted array A is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# 
# Find the minimum element.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        n = len(A)
        return self.rotatedMinSearch(A, 0, n - 1)

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def rotatedMinSearch(self, A, i, j):
        if i > j:
            return A[0]
        mid = int(i + (j - i) / 2)
        if mid < j and A[mid + 1] < A[mid]:
            return A[mid + 1]
        if mid > i and A[mid - 1] > A[mid]:
            return A[mid]
        if A[mid] >= A[i]:
            return self.rotatedMinSearch(A, mid + 1, j)
        return self.rotatedMinSearch(A, i, mid - 1)
