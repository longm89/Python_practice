"""
Given the root of a binary tree, 
imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.


Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        The number of nodes that we could see will be depth of the tree + 1
        For all the nodes with the same height, if we use BFS, the node that we
        see will be such that it's the last node of that height in the queue
        The time complexity is O(N)
        The space complexity is O(N)
        where N is the number of nodes
        We could do BFS level by level so that we don't need to keep track of
        the height
        """

        if not root:
            return []

        queue = [root]
        result = []
        first_pos = 0

        while first_pos < len(queue):
            last_pos = len(queue) - 1
            result.append(queue[-1].val)
            for current_node in queue[first_pos : last_pos + 1]:
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            first_pos = last_pos + 1

        return result
