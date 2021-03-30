"""
Given the root of a binary tree, return the bottom-up level 
order traversal of its nodes' values. 
(i.e., from left to right, level by level from leaf to root).

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        We could use BFS, level by level to find the nodes in each level
        from the left to the right. We store it in a list and then reverse the list
        in the end to have the result.
        The time complexity is O(n) where n is the number of nodes in the tree
        """

        if not root:
            return []

        queue = [root]
        first_pos = 0
        reversed_result = []

        while first_pos < len(queue):
            last_pos = len(queue) - 1
            current_level = []
            for node in queue[first_pos: last_pos+1]:
                current_level.append(node.val)
            reversed_result.append(current_level)

            # add the nodes of the next level
            for node in queue[first_pos: last_pos+1]:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            first_pos = last_pos + 1

        return reversed_result[::-1]


