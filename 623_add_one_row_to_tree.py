# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
Given the root of a binary tree,
then value v and depth d,
you need to add a row of nodes with value v at the given depth d.
The root node is at depth 1.

The adding rule is: given a positive integer depth d,
for each NOT null tree nodes N in depth d-1,
create two tree nodes with value v
as N's left subtree root and right subtree root.
And N's original left subtree should be the left subtree
of the new left subtree root,
its original right subtree should be the right
subtree of the new right subtree root.
If depth d is 1 that means there is no depth d-1 at all,
then create a tree node with value v as the new root of the whole
original tree, and the original tree is the new root's left subtree.
"""


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        """
        If d = 1, add the root to the tree
        If d > 1, find all the nodes at depth d - 1 using BFS, create two nodes
        and add the original left and right subtrees of the node.
        There are 2n edges in a tree with n nodes,
        the time complexity is O(n)
        the space complexity is O(n)
        """
        if d == 1:
            new_node = TreeNode(v, root, None)
            return new_node
        if d > 1:
            # add the node and the depth of the node to the queue
            queue = [(root, 1)]
            start = 0
            while (start <= len(queue) - 1):
                (current_node, current_depth) = queue[start]
                start += 1
                if current_depth < d-1:
                    # if the current_depth < d-1, add the left and right
                    # children to the queue
                    if current_node.left:
                        queue.append((current_node.left, current_depth + 1))
                    if current_node.right:
                        queue.append((current_node.right, current_depth + 1))
                if current_depth == d-1:
                    # if the current depth is d-1, we don't need to add more
                    # nodes into the queue
                    left_child = TreeNode(v, current_node.left, None)
                    right_child = TreeNode(v, None, current_node.right)
                    current_node.left = left_child
                    current_node.right = right_child
        return root
