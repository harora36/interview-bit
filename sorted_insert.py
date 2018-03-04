# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.


class Solution:

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        n = len(A)
        return self.insert(A, B, 0, n - 1)

    # @param B : integer
    # @return a integer
    def insert(self, A, B, i, j):
        if i > j or j < 0:
            return -1
        mid = int((i + (j - i) / 2))
        if A[mid] == B:
            return mid
        if A[mid] < B and (mid == j or A[mid + 1] >= B):
            return mid + 1
        if A[mid] > B and (mid == 0 or A[mid - 1] <= B):
            if mid > 0 and A[mid - 1] == B:
                return mid - 1
            return mid
        elif A[mid] < B:
            return self.insert(A, B, mid + 1, j)
        else:
            return self.insert(A, B, i, mid - 1)
        return -1
