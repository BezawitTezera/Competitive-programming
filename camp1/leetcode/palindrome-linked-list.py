# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        Next = prev = None
        curr = slow

        while curr:
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next

        first = head
        second = prev
        while first and second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
