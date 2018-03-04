# You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
# Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, 
# then the whole array should get sorted.
# If A is already sorted, output -1.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        i = 0
        while i < n - 1 and A[i] <= A[i + 1]:
            i += 1
        if i == n - 1:
            return [-1]
        j = n - 1
        while j > 0 and A[j] >= A[j - 1]:
            j -= 1
        min_ele = float('inf')
        max_ele = float('-inf')
        for k in range(i, j + 1):
            if A[k] < min_ele:
                min_ele = A[k]
            if A[k] > max_ele:
                max_ele = A[k]
        k = 0
        while k <= i and A[k] <= min_ele:
            k += 1
        l = n - 1
        while l >= j and A[l] >= max_ele:
            l -= 1
        answer = list()
        answer.append(k)
        answer.append(l)
        return answer

