"""
Given the head of a linked list, 
remove the nth node from the end of the list and return its head.
Follow up: Could you do this in one pass?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        1) The trivial cases, 
        head == None, return head
        head.next == None, return None
        2) For the general case, we need to find the node at position right
        before the node at the n-position from the end, i.e position n+1 from
        the end, called it prev_target_node. 
        If prev_target_node = None (n = length of the list), return head.next
        if not, put prev_target_node.next = prev_target_node.next.next and 
        return the head

        To do that, we keep 2 pointers:
        first_pointer: at the head position
        second_pointer: at the position n+1, 
        if second_pointed == None, return head.next
        else:
        we move both pointers until second_pointer.next == None, then
        prev_target_node = first_pointer.
        We put first_pointer.next = first_pointer.next.next

        The time complexity is O(length of the list)
        The space complexity is O(1)
        """

        if not head or not head.next:
            return None

        first_pointer = head
        second_pointer = head
        for i in range(n):
            second_pointer = second_pointer.next
        if not second_pointer:
            return head.next

        while second_pointer.next:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        first_pointer.next = first_pointer.next.next

        return head

