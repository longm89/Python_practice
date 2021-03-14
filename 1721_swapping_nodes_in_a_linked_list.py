"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node
from the beginning and the kth node from the end (the list is 1-indexed).


Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Example 3:
Input: head = [1], k = 1
Output: [1]

Example 4:
Input: head = [1,2], k = 1
Output: [2,1]

Example 5:
Input: head = [1,2,3], k = 2
Output: [1,2,3]

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 10**5
0 <= Node.val <= 100

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        """
        We will exchange two nodes at position k from the beginning and k from
        the end, called them node1 and node2
        We will exchange 2 nodes so that node1 appears first before node2
        The general case, the list is of the form:
        ...-> prev1 -> node1 -> ...-> prev2 -> node2 -> ...
        and we want to switch node1 and node2
        To switch 2 nodes, we care about the positions of 4 arrows:
        prev1->node1, node1->node1.next, prev2->node2, node2->node2.next
        and we need to switch these 4 arrows.
        It's possible that the general sequence above degenerates:
            1) prev1 is None: We will need to move the position of the head
            in case prev1 is None after exchanging.
            2) node1 == prev2
            3) node1 == node2 : we check in the beginning, so we will not need
            to do anything
        So to switch 4 arrows, we will do 4 cases of 1) and 2)

        The time complexity is O(n)
        The space complexity is O(1)
        """
        # find prev1, node1, prev2, node2 and check for case 3)
        # call pos_prev1, pos_node1, pos_prev2, pos_node2 the integer numbers
        # representing the positions of the nodes in the list

        # first find prev1, node1, pos_prev1, pos_node1
        prev1 = None
        node1 = head
        pos_prev1 = 0
        pos_node1 = 1
        while pos_node1 < k:
            pos_node1 += 1
            pos_prev1 += 1
            prev1 = node1
            node1 = node1.next

        # find prev2, node2, pos_prev2, pos_node2
        # initialize (prev2, node2, pos_prev2, pos_node2) at position 1, and
        # node3 at position node1 and move the two together until node3
        # is the final node
        prev2 = None
        node2 = head
        pos_prev2 = 0
        pos_node2 = 1
        node3 = node1

        while node3.next:
            pos_node2 += 1
            pos_prev2 += 1
            prev2 = node2
            node2 = node2.next
            node3 = node3.next

        # deal with the cases 1), 2), 3)
        if pos_node1 == pos_node2:
            return head
        
        if pos_node1 > pos_node2:
            pos_prev1, pos_node1, pos_prev2, pos_node2 = pos_prev2,\
                pos_node2, pos_prev1, pos_node1
            prev1, node1, prev2, node2 = prev2, node2, prev1, node1
        # deal with the 4 cases 1) and 2)
        if pos_prev1 == 0:
            if pos_node1 == pos_prev2:
                node1.next, node2.next = node2.next, node1
            else:
                node1.next, node2.next, prev2.next = node2.next, node1.next,\
                    node1
            head = node2
        else:
            if pos_node1 == pos_prev2:
                prev1.next, node1.next, node2.next = node2, node2.next, node1
            else:
                prev1.next, node1.next, node2.next, prev2.next = node2,\
                    node2.next, node1.next, node1

        return head
