"""
Given an integer array nums, return the length of the longest wiggle sequence.

A wiggle sequence is a sequence where the differences between successive 
numbers strictly alternate between positive and negative. 
The first difference (if one exists) may be either positive or negative. 
A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence 
because the differences (6, -3, 5, -7, 3) 
are alternately positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, 
the first because its first two differences are positive and 
the second because its last difference is zero.
A subsequence is obtained by deleting some elements (eventually, also zero) 
from the original sequence, leaving the remaining elements in 
their original order.

 

Example 1:
Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.

Example 2:
Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Example 3:
Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
"""


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        Let down[end_pos] be the length of the longest sequence,
        ending at nums[end_pos], such that down[end_pos] is less than the
        previous number in the sequence
        Let up[end_pos] be the length of the longest sequence,
        ending at nums[end_pos], such that up[end_pos] is bigger than the
        previous number in the sequence
        We have then:
        down[end_pos] = 1 + max (up[i]),
        where 0 <= i <= end_pos-1, nums[end_pos] < nums[i]
        up[end_pos] = 1 + max (down[i]),
        where 0 <= i <= end_pos-1, nums[end_pos] > nums[i]

        The final result is max(down[i],up[i] for all 0 <=i <= len(nums)-1)

        The time complexity is O(len(nums)**2)
        The space complexity is O(len(nums))
        There exists an O(len(nums)) algorithm.
        """

        down = [1 for i in range(len(nums))]
        up = [1 for i in range(len(nums))]

        for end_pos in range(1, len(nums)):
            for i in range(0, end_pos):
                if nums[end_pos] > nums[i]:
                    up[end_pos] = max(up[end_pos], down[i] + 1)
                elif nums[end_pos] < nums[i]:
                    down[end_pos] = max(down[end_pos], up[i] + 1)
        max_length = 0

        for i in range(len(nums)):
            max_length = max(max_length, up[i])
            max_length = max(max_length, down[i])

        return max_length
