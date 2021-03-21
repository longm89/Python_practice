"""
Given the root of a binary tree and an integer targetSum, 
return all root-to-leaf paths where each path's sum equals targetSum.
A leaf is a node with no children.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:

        """
        We will use BFS to solve this problem.
        We implement it using a queue.
        Each element in the queue is of the form (current_node, total_sum),
        where total_sum is the sum of the root to the current_node
        To trace the paths, we keep a prev_list, where
        prev_list[i] = j means the previous node of queue[i][0] is queue[j][0]
        """

        if not root:
            return []

        queue = []
        queue.append((root, root.val))
        first_pos = 0
        prev_list = [-1]
        output = []

        while first_pos < len(queue):
            current_node, total_sum = queue[first_pos]
            if current_node.left:
                queue.append((current_node.left, total_sum + current_node.left.val))
                prev_list.append(first_pos)
            if current_node.right:
                queue.append((current_node.right, total_sum + current_node.right.val))
                prev_list.append(first_pos)
            first_pos += 1

        for index in range(len(queue)):
            element = queue[index]
            if not element[0].left and not element[0].right:
                if element[1] == targetSum:
                    path = []
                    current_node = element[0]
                    current_index = index
                    while current_index != -1:
                        path.append(current_node.val)
                        current_index = prev_list[current_index]
                        current_node = queue[current_index][0]
                    output.append(path[::-1])

        return output
