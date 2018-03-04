# Given a non-negative number represented as an array of digits,
# 
# add 1 to the number ( increment the number represented by the digits ).

class Solution:
    def plusOne(self, A):
        n = len(A)
        carry = 1
        for i in range(n-1, -1, -1):
            A[i] += carry
            carry = int(A[i] / 10)
            A[i] = int(A[i] % 10)

        i = 0
        output = []
        if carry == 0:
            while i < n and A[i] == 0:
                i += 1
        else:
            output.append(carry)
        while i < n:
            output.append(A[i])
            i += 1
        return output
