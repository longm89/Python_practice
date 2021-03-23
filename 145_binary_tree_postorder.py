"""
Given the root of a binary tree, 
return the postorder traversal of its nodes' values.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        We will use DFS to traverse the tree.
        We will implement DFS using a stack.
        For DFS postorder, we will traverse the left subtree,
        the right subtree, and then we process the data of the node
        Each element of the stack is of the form [curr_node, left_visited, right_visited]
        where left_visited and right_visited mark whether we have travelled down the left
        child or the right child
        """

        if not root:
            return []

        stack = [[root, False, False]]
        visited_values = []

        while stack:
            curr_node, left_visited, right_visited = (
                stack[-1][0],
                stack[-1][1],
                stack[-1][2],
            )

            if left_visited and right_visited:
                visited_values.append(curr_node.val)
                stack.pop()
                continue

            if not right_visited:
                stack[-1][2] = True
            if not left_visited:
                stack[-1][1] = True
            if curr_node.right:
                stack.append([curr_node.right, False, False])
            if curr_node.left:
                stack.append([curr_node.left, False, False])

        return visited_values
