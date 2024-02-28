# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        ans = []
        curr = head
        count = 1
        while curr.next != None:
            count += 1
            curr = curr.next
                
        mid = count // 2
        curr = head
        for i in range(mid):
            curr = curr.next
        return curr
