class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        pos = 0               # find the starting position
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                pos = i

        new_nums = list()
        for i in range(pos,len(nums)):
            new_nums.append(nums[i])
        for i in range(0,pos):
            new_nums.append(nums[i])
        start = 0
        end = len(nums)-1
        while start<=end:
            middle = (start+end)//2
            if new_nums[middle] == target:
                return True
            elif new_nums[middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        return False

        
