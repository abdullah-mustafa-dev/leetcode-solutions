# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        check = set()
        trav = head
        while trav:
            if trav in check:
                return True
            check.add(trav)
            trav = trav.next
        return False