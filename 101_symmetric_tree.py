# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(tree1,tree2):
            if (not tree1) and (not tree2):
                return True
            if (not tree1) or (not tree2):
                return False
            return (tree1.val == tree2.val) and check(tree1.left,tree2.right) and check(tree1.right,tree2.left)
        return check(root,root)
