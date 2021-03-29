"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of
every node differ in height by no more than 1.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        We use DFS to determine the heights of each node in the tree
        if the node is a leaf, the height is 0,
        The height of a node is 1 + the max height of the left and right
        children
        """

        def DFS_height(node):
            """
            return the height of the node if the tree is balanced
            return -2 if not
            """

            left_height = -1
            right_height = -1
            if node.left:
                left_height = DFS_height(node.left)
            if node.right:
                right_height = DFS_height(node.right)
            if left_height == -2 or right_height == -2:
                return -2
            if abs(left_height-right_height) >= 2:
                return -2

            return max(left_height, right_height) + 1

        if not root:
            return True
        return DFS_height(root) != -2


