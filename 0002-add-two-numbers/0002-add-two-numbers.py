# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t = ListNode()
        tm = t
        carry = 0
        while(l1 and l2):
            summ = (l1.val + l2.val + carry)
            t.next = ListNode(summ % 10)
            carry = summ // 10
            l1 = l1.next
            l2 = l2.next
            t = t.next
        
        while l1:
            summ = (l1.val + carry)
            t.next = ListNode(summ % 10)
            carry = summ // 10
            l1 = l1.next
            t = t.next

        while l2:
            summ = (l2.val + carry)
            t.next = ListNode(summ % 10)
            carry = summ // 10
            l2 = l2.next
            t = t.next
        
        if carry != 0:
            t.next = ListNode(carry)
        
        return tm.next