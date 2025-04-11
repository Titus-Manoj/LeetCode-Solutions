# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # Find the middle of the list
        mid = self.findMid(head)
        right = mid.next
        mid.next = None
        left = head

        # Recursively sort the two halves
        left = self.sortList(left)
        right = self.sortList(right)
        # Merge the sorted halves
        ans = self.merge(left, right)
        return ans

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        temp = dummy
        # Merge the two lists in sorted order
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                temp = list1
                list1 = list1.next
            else:
                temp.next = list2
                temp = list2
                list2 = list2.next
        # Attach the remaining elements
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2

        return dummy.next

    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        # Fast moves twice as fast as slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow