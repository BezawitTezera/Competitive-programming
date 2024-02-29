# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = ListNode()
        greater = ListNode()

        first = smaller
        second = greater

        curr = head
        while curr:
            if curr.val < x:
                first.next = curr
                first = first.next
            else:
                second.next = curr
                second = second.next

            curr = curr.next

        first.next = greater.next
        second.next = None
        return smaller.next