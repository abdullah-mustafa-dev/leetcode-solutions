# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return False
    
        def helper(l=root.left, r=root.right):
            if not l and not r:
                return True
            if not l and r or l and not r:
                return False
            
            if l.val == r.val:
                return helper(l.left, r.right) and helper(l.right, r.left)
            else:
                return False
        return helper()
        