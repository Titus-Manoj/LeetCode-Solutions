# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        ans = head
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        while(l1 != None and l2 != None):
            if l1.val > l2.val:
                head.next = ListNode(l2.val)
                l2 = l2.next
            else:
                head.next = ListNode(l1.val)
                l1 = l1.next
            head = head.next
        
        if l1 != None:
            head.next = l1
        
        if l2 != None:
            head.next = l2
        
        return ans.next
