# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def rob_recursion(node):  # return max_yes, max_not
            if not node:
                return 0,0
            # calculate max_yes
            max_yes_left, max_not_left = rob_recursion(node.left)
            max_yes_right, max_not_right = rob_recursion(node.right)

            max_yes = node.val + max_not_left + max_not_right
            max_not = max(max_not_left,max_yes_left) + max(max_not_right,max_yes_right)

            return max_yes,max_not

        max_yes, max_not = rob_recursion(root)
        return max(max_yes, max_not)
