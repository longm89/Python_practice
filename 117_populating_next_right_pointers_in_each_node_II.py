"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        array = list()
        start = 0
        array.append(root)
        while start < len(array):
            for i in range(start, len(array) - 1):
                array[i].next = array[i+1]
            array[-1].next = None

            n = len(array)
            for i in range(start, n):
                node = array[i]
                if node.left:
                    array.append(node.left)
                if node.right:
                    array.append(node.right)

            start = n

        return root
        
