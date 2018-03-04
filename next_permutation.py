# Implement the next permutation, which rearranges numbers into the numerically next greater permutation of
# numbers.
# 
# If such arrangement is not possible, it must be rearranged as the lowest possible order ie, sorted 
# in an ascending order.


class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        n = len(A)
        j = n - 1
        while j > 0:
            if A[j] > A[j-1]:
                break
            else:
                j -= 1
        j = j-1
        i = n-1
        while i > j:
            if A[i] > A[j]:
                break
            i -= 1
        if j < 0 or i <= j:
            return sorted(A)
        t = A[i]
        A[i] = A[j]
        A[j] = t
        start = j + 1
        end = n-1
        while start < end:
            t = A[start]
            A[start] = A[end]
            A[end] = t
            start += 1
            end -= 1
        return A
