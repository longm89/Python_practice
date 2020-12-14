class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def Is_starting_index(arr, index):  # check if index is the starting index of the array arr
        # check the case when len(arr) == 1
            if len(arr) == 1 and index == 0:
                return True

            at_0 = (index == 0) and (arr[0] < arr[1])
            at_last = (index == len(arr) - 1) and (arr[index] < arr[index - 1])
            at_middle = (0 < index) and (index < len(arr) - 1) and (arr[index - 1] > arr[index]) and (arr[index + 1] > arr[index])
            return at_0 or at_last or at_middle

    # First step: Finding the starting index of a rotated sorted array arr
        def Find_starting_index(arr):
            min_index = 0
            max_index = len(arr) - 1
            while (min_index <= max_index):
                if arr[min_index] <= arr[max_index]:
                    return min_index
                mid = (min_index + max_index) // 2
                if Is_starting_index(arr, mid):
                    return mid
                if arr[mid] >= arr[0]:
                    min_index = mid + 1
                else:
                    max_index = mid
    # Second step:
        n = len(nums)
        start_index = Find_starting_index(nums)
        end_index = start_index + n - 1
        while start_index <= end_index:
            mid = (start_index + end_index) // 2
            if nums[mid % n] == target:
                return mid % n
            if nums[mid % n] > target:
                end_index = mid - 1
            else:
                start_index = mid + 1
        return -1
