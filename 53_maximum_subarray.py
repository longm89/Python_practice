class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        total_sum = 0
        min_sum = 0
        largest_sum = - (2**31 - 1)
        for value in nums:
            total_sum += value
            largest_sum = max(largest_sum, total_sum - min_sum)
            min_sum = min(min_sum,total_sum)
        return largest_sum
