class Solution:
    def isPossible(self, C, n, k, val):
        number_of_painters = 1
        sum = 0
        for i in range(n):
            sum += C[i]
            if sum > val:
                number_of_painters += 1
                sum = C[i]
        return number_of_painters <= k

    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def paint(self, A, B, C):
        start = max(C)
        end = sum(C)
        n =  len(C)
        while start < end:
            mid = int(start + (end - start) / 2)
            if self.isPossible(C, n, A, mid):
                end = mid
            else:
                start = mid + 1
        return (start * B) % 10000003
