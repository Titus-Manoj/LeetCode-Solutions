# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        tmp = head.next
        head.next = None
        def recur(head, tmp):
            if tmp == None:
                return head
            t = tmp.next
            tmp.next = head
            return recur(tmp, t)
        return recur(head, tmp)