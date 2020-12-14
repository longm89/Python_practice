class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = list()
        result.append(nums)
        new_permutation = nums
        while True:
            # check if I could find a new permutation
            Pos_found = -1
            for i in range(len(nums)-1,0,-1):
                if nums[i]>nums[i-1]:
                    Pos_found = i
                    break
            if Pos_found == -1:
                break
            min_Pos = Pos_found
            while (min_Pos<len(nums)-1) and (nums[min_Pos+1]>nums[Pos_found - 1]):
                min_Pos += 1
            new_permutation = nums[0:Pos_found-1]
            new_permutation.append(nums[min_Pos])
            for i in range(len(nums)-1,min_Pos,-1):
                new_permutation.append(nums[i])
            new_permutation.append(nums[Pos_found-1])
            for i in range(min_Pos-1,Pos_found-1,-1):
                new_permutation.append(nums[i])
            result.append(new_permutation)
            nums = new_permutation
        return result


        
