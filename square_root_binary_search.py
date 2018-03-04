# Implement int sqrt(int x).
# 
# Compute and return the square root of x.
# 
# If x is not a perfect square, return floor(sqrt(x))

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A

        # Do Binary Search for floor(sqrt(x))
        start = 1
        end = A
        while start <= end:
            mid = (start + end) / 2
            if mid * mid == A:
                return mid

            if mid * mid < A:
                start = mid + 1
                square_root = mid
            else:
                end = mid - 1
        return int(square_root)
