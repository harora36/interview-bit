class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        n = len(A)
        m = len(A[0])
        minimum = A[0][0]
        maximum = A[0][0]
        for i in range(n):
            if A[i][0] < minimum:
                minimum = A[i][0]
            if A[i][m - 1] > maximum:
                maximum = A[i][m - 1]
        mid_count = int((n * m + 1) / 2)
        while minimum < maximum:
            mid = int(minimum + (maximum - minimum) / 2)
            count = 0
            for i in range(n):
                c, isPresent = self.findLessCount(A[i], m, mid)
                if isPresent:
                    while c < m and A[i][c] == mid:
                        c += 1
                    count += c
                else:
                    count += c + 1
            if count < mid_count:
                minimum = mid + 1
            else:
                maximum = mid
        return minimum

    def findLessCount(self, A, n, val):
        start = 0
        end = n - 1
        while start <= end:
            mid = int((start + end) / 2)
            if A[mid] == val:
                return mid, True
            if A[mid] < val:
                if mid + 1 >= n or A[mid + 1] > val:
                    return mid, False
                start = mid + 1
            if A[mid] > val:
                if mid - 1 < 0 or A[mid - 1] < val:
                    return mid - 1, False
                end = mid - 1
        return start, False
