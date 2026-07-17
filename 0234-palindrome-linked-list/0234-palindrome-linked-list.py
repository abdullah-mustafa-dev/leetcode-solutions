# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        pre = None
        fast = slow = head
        size = 1
        while fast and fast.next:
            fast = fast.next.next
            size += 2
            nxt = slow.next
            slow.next = pre
            pre = slow
            slow = nxt

        size += 1 if fast is None else 0

        p1 = pre
        p2 = slow if size % 2 == 0 else slow.next
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1, p2 = p1.next, p2.next
        return p1 == p2