"""
You are given a perfect binary tree where all leaves 
are on the same level, and every parent has two children. 
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. 
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space 
does not count as extra space for this problem.
"""


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":

        """
        We could use DFS and recursion to populate the nodes:
        DFS_populate_right(node):
        if node.left and node.right:
            node.left.next = node.right
            we still need to populate node.right:
                we need to point node.right.next to
                node.next.left in case node.next exists.
        """

        def DFS_populate_right(node):
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                DFS_populate_right(node.left)
                DFS_populate_right(node.right)

        if not root:
            return None

        DFS_populate_right(root)

        return root
