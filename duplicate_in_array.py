# Given a read only array of n + 1 integers between 1 and n, find one number that repeats in linear
# time using less than O(n) space and traversing the stream sequentially O(1) times.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        count1 = 0
        a = None
        numbers = {}
        for i in range(n):
            numbers[A[i]] = numbers.get(A[i], 0) + 1
        answer = -1
        for i in range(n):
            if numbers[A[i]] > 1:
                answer = A[i]
        return answer
