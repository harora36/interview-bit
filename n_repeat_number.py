# You’re given a read only array of n integers. Find out if any integer occurs more than n/3 times
# in the array in linear time and constant additional space.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        n = len(A)
        count1 = 0
        count2 = 0
        a = None
        b = None
        no = {}
        for i in range(n):
            no[A[i]] = no.get(A[i], 0) + 1
            if a == A[i]:
                count1 += 1
                a = A[i]
            elif b == A[i]:
                count2 += 1
                b = A[i]
            elif count1 == 0:
                count1 = 1
                a = A[i]
            elif count2 == 0:
                count2 = 1
                b = A[i]
            else:
                count1 -= 1
                count2 -= 1
        count1 = 0
        count2 = 0
        for i in range(n):
            if a == A[i]:
                count1 += 1
            elif b == A[i]:
                count2 += 1
        answer = None
        if count1 > n / 3:
            answer = a
        elif count2 > n / 3:
            answer = b
        return -1 if not answer else answer
