class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sums = sum(nums)
        if sums % 2 != 0:
            return False
        target = sums // 2
        f = set()
        f.add(0)
        for i in range(len(nums)):
            g = f.copy()
            for x in g:
                if x + nums[i] not in f:
                    f.add( x + nums[i])
            if target in f:
                return True
        return False
