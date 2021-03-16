"""
Given an array of unique integers, arr, where each integer arr[i] is strictly
greater than 1. We make a binary tree using these integers, and each number
may be used for any number of times. Each non-leaf node's value should be 
equal to the product of the values of its children. Return the number of 
binary trees we can make. The answer may be too large so return the 
answer modulo 10**9 + 7.

Example 1:
Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Example 2:
Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

Constraints:

1 <= arr.length <= 1000
2 <= arr[i] <= 10**9
"""


class Solution:
    def numFactoredBinaryTrees(self, arr) -> int:
        """
        We get a sorted array without repeating value sorted_arr from arr
        We keep a dict_nums: dict_nums[val] is the index of sorted_arr with
        value val
        Let num_of_trees(i) be the number of trees with the root having
        value sorted_arr[i]. To calculate num_of_trees(sorted_arr[i]):
        There's one tree if the root has no children
        If there exist i1 < i such that sorted_arr[i] % sorted_arr[i1] == 0,
            if val2= sorted_arr[i]//sorted_arr[i1] is in dict_nums,
        then they give rise to num_of_trees(i1) * num_of_trees(dict_nums[val2]) trees

        We could use dynamic programming to calculate num_of_trees(i) where i
        is from 1 to len(sorted_arr)
        The time complexity is O(len(arr)**2)

        """

        sorted_arr = list(set(arr))
        sorted_arr.sort()

        dict_nums = dict()
        for i in range(len(sorted_arr)):
            dict_nums[sorted_arr[i]] = i

        # if the root has no children, the number of trees is 1
        num_of_trees = [1 for i in range(len(sorted_arr))]

        for i in range(len(sorted_arr)):
            for i1 in range(0, i):
                if sorted_arr[i] % sorted_arr[i1] == 0:
                    val2 = sorted_arr[i] // sorted_arr[i1]
                    if val2 in dict_nums:
                        num_of_trees[i] += (
                            num_of_trees[i1] * num_of_trees[dict_nums[val2]]
                        )
        num_of_trees[i] %= 10 ** 9 + 7

        total_trees = 0
        for num in num_of_trees:
            total_trees += num
            total_trees %= 10 ** 9 + 7

        return total_trees
