# Given a positive integer n and a string s consisting only of letters D or I, you have to 
# find any permutation of first n positive integer that satisfy the given input string.
# 
# D means the next number is smaller, while I means the next number is greater.

class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        max_ele = B
        min_ele = 1
        res = list()
        for i in range(B - 1):
            if A[i] == 'I':
                res.append(min_ele)
                min_ele += 1
            else:
                res.append(max_ele)
                max_ele -=1
        res.append(min_ele)
        return res
