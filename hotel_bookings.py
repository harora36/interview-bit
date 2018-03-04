# A hotel manager has to process N advance bookings of rooms for the next season. His hotel has K rooms.
# Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms 
# in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .


class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        n = len(arrive)
        bookings ={}
        for i in range(n):
            bookings[arrive[i]] = 1 + bookings.get(arrive[i], 0)
            bookings[depart[i]] = -1 + bookings.get(depart[i], 0)

        count = 0
        keys = bookings.keys()
        keys = sorted(keys)
        for key in keys:
            count += bookings.get(key)
            if count > K:
                return False
        return count <= K
