# Given a collection of intervals, merge all overlapping intervals.

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        n = len(intervals)
        if n <= 1:
            return intervals
        result = list()
        intervals.sort(key=lambda interval: interval.start)
        result.append(intervals[0])
        prv = 0
        for i in range(1, n):
            prv_interval = result[prv]
            if intervals[i].start <= prv_interval.end or intervals[i].end <= prv_interval.end:
                result[prv] = Interval(prv_interval.start, max(intervals[i].end, prv_interval.end))
            else:
                result.append(intervals[i])
                prv += 1

        return result
