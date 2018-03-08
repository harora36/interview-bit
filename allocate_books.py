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

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        start = max(A)
        end = sum(A)
        n = len(A)
        if n < B:
            return -1
        if n == B:
            return start
        result = float('inf')
        while start <= end:
            mid = int(start + (end - start) / 2)
            if self.isPossible(A, n, B, mid):
                result = min(result, mid)
                end = mid - 1
            else:
                start = mid + 1
        return result if result != float('inf') else -1
