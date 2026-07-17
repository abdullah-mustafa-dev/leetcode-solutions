# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = fast = head
        first = True
        while True:
            if not first and slow == fast:
                return True
            elif fast is None or fast.next is None:
                return False    
            first = False

            slow = slow.next
            fast = fast.next.next