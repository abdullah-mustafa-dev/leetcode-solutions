# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        size_a = size_b = 0
        pa = headA
        pb = headB
        while pa or pb:
            if pa:
                size_a += 1
                pa = pa.next
            if pb:
                size_b += 1 
                pb = pb.next

        diff = abs(size_a - size_b)
        p1, p2 = headA, headB
        while diff:
            if size_a < size_b:
                p2 = p2.next
            else:
                p1 = p1.next
            diff -= 1

        while p1 and p2:
            if p1 and p1 == p2:
                return p1
            p1, p2 = p1.next, p2.next

        return None