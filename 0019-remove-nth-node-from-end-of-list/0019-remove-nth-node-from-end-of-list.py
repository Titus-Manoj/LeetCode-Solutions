# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        t = ListNode(0, head)
        fast = t
        slow = t
        if head.next == None:
            return None
        while(n>-1 and fast):
            fast = fast.next
            n -= 1
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return t.next