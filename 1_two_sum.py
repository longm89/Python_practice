class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_of_nums = dict()
        for key,value in enumerate(nums):
            u = target - value
            if u in index_of_nums:
                return [key, index_of_nums[u]]
            index_of_nums[value] = key
            
