# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        size = 0
        trav = head
        while trav:
            size += 1
            trav = trav.next

        if size - n == 0:
            return head.next
        
        cur = head
        idx = 1
        while cur:
            if size - n == idx:
                cur.next = cur.next.next
                return head
            cur = cur.next
            idx += 1