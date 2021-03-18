"""
11. Container With Most Water

Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of
the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container,
such that the container contains the most water.
Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are
represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section)
the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2
 
Constraints:

n == height.length
2 <= n <= 10**5
0 <= height[i] <= 10**4
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        In general, we need to check n^2 pairs of start_pos and end_pos

        We have some remarks:

        1) given a start_pos, we will need to check the area formed by the rectangle
        at start_pos and end_pos = len(height)-1. The next ending position to
        check will be such that height(next_end_pos) > height(end_pos).

        2) For the starting point, after we check the start_pos,
        the next next_start_pos to check will be such that
        height(next_start_pos) > height(start_pos)
        From 1), 2), we can assume that the heights will be of the form:
        a1 < a2 < a3 <....< ak > a(k-1) > a(k-2) >....> an

        3) For a position start_pos, we will only need to look at the end_pos from prev_end_pos until
        height(next_end_pos) > height(start_pos)

        The time complexity is O(len(height))
        The space complexity is O(1)
        """

        prev_start_pos = -1
        end_pos = len(height) - 1
        max_water = 0

        for start_pos in range(0, len(height)):
            # only check start_pos such that
            # height[start_pos] > height(prev_start_pos)
            if prev_start_pos == -1 or height[start_pos] > height[prev_start_pos]:
                while height[end_pos] < height[start_pos]:
                    max_water = max(max_water, height[end_pos] * (end_pos - start_pos))
                    end_pos -= 1
                if end_pos > start_pos:
                    max_water = max(
                        max_water, height[start_pos] * (end_pos - start_pos)
                    )
                else:
                    return max_water
                prev_start_pos = start_pos

        return max_water
