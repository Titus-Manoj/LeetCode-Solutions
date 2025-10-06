# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t1 = head
        t2 = head
        while(t2 != None and t2.next != None):
            t2 = t2.next.next
            t1 = t1.next
        return t1
