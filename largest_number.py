# Given a list of non negative integers, arrange them such that they form the largest number.

class Solution:

    def compare_string(self, a, b):
        str1 = str(a)+str(b)
        str2 = str(b)+str(a)
        if str1 > str2:
            return -1
        return 0

    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        a = sorted(A, cmp=self.compare_string)
        n = len(a)
        result = ""
        i = 0
        while i < n and a[i]== 0:
            i += 1
        if i >= n :
            return "0"
        for i in range(n):
            result += str(a[i])
        return result
