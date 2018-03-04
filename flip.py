# You are given a binary string(i.e. with characters 0 and 1) S consisting of characters S1, S2, …, SN. In a single operation, you can choose two indices L and R such that 1 ≤ L ≤ R ≤ N and flip the characters SL, SL+1, …, SR. By flipping, we mean change character 0 to 1 and vice-versa.
# 
# Your aim is to perform ATMOST one operation such that in final string number of 1s is maximised. If you don’t want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.


class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        n = len(A)
        max_len = 0
        curr_len = 0
        curr_sum = 0
        max_sum = -1
        start = -1
        end = 0
        max_start = -1
        max_end = -1
        for i in range(n):
            curr_sum = curr_sum + (-1 if A[i] == '1' else 1)
            if curr_sum < 0:
                curr_sum = 0
                start = -1
            else:
                if start == -1:
                    start = i + 1
                end = i + 1
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    max_start = start
                    max_end = end


        result = []
        if max_start == -1:
            return []
        result.append(max_start)
        result.append(max_end)
        return result

