# Given a sorted array of integers, find the starting and ending position of a given target value.
# 
# Your algorithm’s runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].

class Solution:

    # @param A : tuple of integers
    # @param B : integer
    # @return a integer
    def search_first(self, A, B, i, j):
        if i > j or j < 0:
            return -1
        mid = int((i + (j-i)/2))
        if A[mid] == B and (mid == 0 or A[mid - 1] < B):
            return mid
        if A[mid] < B:
            return self.search_first(A, B, mid + 1, j)
        else:
            return self.search_first(A, B, i, mid - 1)
        return -1

    # @param A : tuple of integers
    # @param B : integer
    # @return a integer
    def search_last(self, A, B, i, j):
        if i > j or j < 0:
            return -1
        mid = int((i + (j - i) / 2))
        if A[mid] == B and (mid == j or A[mid + 1] > B):
            return mid
        if A[mid] <= B:
            return self.search_last(A, B, mid + 1, j)
        else:
            return self.search_last(A, B, i, mid - 1)
        return -1

    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        i = 0
        j = len(A) - 1
        start = self.search_first(A, B, i, j)
        if start == -1:
            return [-1, -1]
        end = self.search_last(A, B, start, j)
        return [start, end]
