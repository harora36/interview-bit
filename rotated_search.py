# Suppose a sorted array is rotated at some pivot unknown to you beforehand.
# 
# (i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).
# 
# You are given a target value to search. If found in the array, return its index, otherwise return -1.


class Solution:

    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        n = len(A)
        return self.rotatedSearch(A, B, 0, n - 1)

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def rotatedSearch(self, A, B, i, j):
        if i > j:
            return -1
        mid = int(i + (j-i)/2)
        if A[mid] == B:
            return mid
        if A[i] <= A[mid]:
            if A[i] <= B <= A[mid]:
                return self.rotatedSearch(A, B, i, mid - 1)
            return self.rotatedSearch(A, B, mid + 1, j)

        if A[mid] <= B <= A[j]:
            return self.rotatedSearch(A, B, mid + 1, j)
        return self.rotatedSearch(A, B, i, mid - 1)
