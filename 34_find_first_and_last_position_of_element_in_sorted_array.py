class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def find_first(arr,number):
            start = 0
            end = len(arr) - 1
            while start <= end:
                middle = (start + end)//2
                if (arr[middle] == number) and ((middle ==0) or (middle > 0 and arr[middle - 1] != number)):
                    return middle
                if arr[middle] > number:
                    end = middle - 1
                elif arr[middle] < number:
                    start = middle + 1
                else:
                    end = middle
            return -1

        def find_last(arr,number):
            start = 0
            end = len(arr) - 1
            while start <= end:
                middle = (start + end + 1)//2
                if (arr[middle] == number) and ((middle == len(arr)-1) or (middle < len(arr)-1 and arr[middle + 1] != number) ):
                    return middle
                if arr[middle] < number:
                    start = middle + 1
                elif arr[middle] > number:
                    end = middle - 1
                else:
                    start = middle
            return -1
        return [find_first(nums,target),find_last(nums,target)]
