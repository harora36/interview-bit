# You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.

class Solution:
    def calculate(self, point1, point2):
        return max(abs(point1[0] - point2[0]), abs(point1[1] - point2[1]))

    def cover_points(self, A, B):
        n = len(A)
        steps = 0
        points = []
        for i in range(0, n):
            points.append(tuple([A[i], B[i]]))
        for i in range(n - 1):
            steps += self.calculate(points[i], points[i + 1])
        return steps
