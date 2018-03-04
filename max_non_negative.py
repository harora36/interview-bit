 # Find out the maximum sub-array of non negative numbers from an array.
 
 class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        n = len(A)
        max_len = 0
        curr_len = 0
        curr_sum = 0
        max_sum = 0
        start = 0
        end = 0
        max_start = -1
        max_end = -1
        for i in range(n):
            if A[i] >= 0:
                if curr_len == 0:
                    start = i
                curr_len += 1
                curr_sum += A[i]
                end = i
            if A[i] < 0 or i == n-1:
                if curr_sum > max_sum:
                    max_len = curr_len
                    max_sum = curr_sum
                    max_start = start
                    max_end = end
                    curr_len = 0
                    curr_sum = 0
                elif curr_sum == max_sum and curr_len > max_len:
                    max_len = curr_len
                    max_start = start
                    max_end = end
                    curr_len = 0
                    curr_sum = 0
                else:
                    curr_len = 0
                    curr_sum = 0

        result = []
        if max_start == -1:
            return []
        for i in range(max_start, max_end + 1):
            result.append(A[i])
        return result
