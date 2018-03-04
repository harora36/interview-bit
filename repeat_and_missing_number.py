class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        xor = 0
        for i in range(1, n + 1):
            xor = xor ^ i
        for i in range(n):
            xor = xor ^ A[i]

        x = 0
        y = 0
        last_set_bit = xor & ~(xor - 1)
        for i in range(n):
            if A[i] & last_set_bit:
                x = x ^ A[i]
            else:
                y = y ^ A[i]
        for i in range(1, n + 1):
            if i & last_set_bit:
                x = x ^ i
            else:
                y = y ^ i
        repeat = 0
        for i in range(n):
            if A[i]^x == 0:
                repeat = x
                missing = y
            elif A[i] ^ y  == 0:
                repeat = y
                missing = x
        result = list()
        result.append(repeat)
        result.append(missing)
        return result
