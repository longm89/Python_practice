"""
Given the root of a binary tree, 
return the leftmost value in the last row of the tree.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """
        We will use BFS to go level by level
        We travel from right to left and save the value of the last node in 
        the tree
        The time complexity is O(number of nodes)
        """

        left_most_value = None
        queue = [root]
        first_pos = 0

        while first_pos < len(queue):
            current_node = queue[first_pos]
            left_most_value = current_node.val
            first_pos += 1
            if current_node.right:
                queue.append(current_node.right)
            if current_node.left:
                queue.append(current_node.left)

        return left_most_value
