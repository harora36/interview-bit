# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxSubArray(self, A):
	    max_so_far = A[0]
	    curr_max = A[0]
	    size = len(A)
	    for i in range(1, size):
	        curr_max = max(A[i], curr_max + A[i])
	        max_so_far = max(max_so_far, curr_max)
	    return max_so_far
