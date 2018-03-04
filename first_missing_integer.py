# Given an unsorted integer array, find the first missing positive integer.

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        ans = [0 for i in range(n + 1)]
        for i in range(n):
            if A[i] >= 0 and A[i] <= n:
                ans[A[i]] = 1
        missing = -1
        present = 0
        for i in range(1, n + 1):
            if ans[i] == 0:
                missing = i
                break
            present = i
        if missing == -1:
            missing = present + 1
        return missing
