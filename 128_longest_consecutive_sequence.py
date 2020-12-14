class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return 0
        num_set = set(nums)
        answer = 1
        for x in num_set:
            if not (x-1 in num_set):
                count =1
                start = x
                while start+1 in num_set:
                    start = start + 1
                    count +=1
                if answer<count:
                    answer = count
        return answer
