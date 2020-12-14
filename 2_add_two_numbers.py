# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry_on = 0
        head = None
        last = None
        while l1 or l2:
            x_1 = 0
            x_2 = 0
            if l1 is None:
                x_1 = 0
            else:
                x_1 = l1.val
                l1 = l1.next
            if l2 is None:
                x_2 =0
            else:
                x_2 = l2.val
                l2 = l2.next
            new_node = None
            if x_1 + x_2 + carry_on>9:
                new_node = ListNode(x_1 + x_2 + carry_on-10, None)
                carry_on = 1
            else:
                new_node = ListNode(x_1 + x_2 + carry_on, None)
                carry_on = 0
            if last is None:
                head = new_node
                last = new_node
            else:
                last.next = new_node
                last = new_node
        if carry_on >0:
            new_node = ListNode(1, None)
            last.next = new_node
        return head


        
