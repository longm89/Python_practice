"""
A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times (possibly zero):

Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].
Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.

 

Example 1:

Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true

Example 2:

Input: triplets = [[1,3,4],[2,5,8]], target = [2,5,8]
Output: true
Explanation: The target triplet [2,5,8] is already an element of triplets.
Example 3:

Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. 
Update the third triplet to be [max(2,1), max(5,2), max(3,5)] = [2,5,5]. 
triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. 
Update the fourth triplet to be [max(2,5), max(5,2), max(5,3)] = [5,5,5]. 
triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.
Example 4:

Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element 
because there is no 2 in any of the triplets.
 

Constraints:

1 <= triplets.length <= 105
triplets[i].length == target.length == 3
1 <= ai, bi, ci, x, y, z <= 1000
"""


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        we could go through all triplets [a_i, b_i, c_i] with
        a_i <= target[0], b_i <= target[1], c_i <= target[2]
        and look for max(a_i), max(b_i), max(c_i).
        If in the end, it's equal to target, then we return True
        The time complexity is O(len(triples)), the space complexity is O(1)
        """
        max_a, max_b, max_c = 0, 0, 0
        for triplet in triplets:
            if (
                triplet[0] <= target[0]
                and triplet[1] <= target[1]
                and triplet[2] <= target[2]
            ):
                max_a = max(max_a, triplet[0])
                max_b = max(max_b, triplet[1])
                max_c = max(max_c, triplet[2])

        return max_a == target[0] and max_b == target[1] and max_c == target[2]


"""
Test: 
1) triplets = [[1, 2, 3], [2, 3, 4], [1, 3, 5], [6, 4, 2]] target = [2, 4, 3]
return False
2) triplets = [[1, 1, 1], [2, 3, 4], [3, 5, 1]] target = [3, 5, 4]
return True
3) triplets = [[1, 4, 5], [1, 2, 3], [4, 2, 1], [3, 2, 1]] target = [1, 2, 3]
return True
"""
