# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def helper(current, low=float('-inf'), high=float('+inf')):
            if not current:
                return True
            
            if current.val <= low or current.val >= high:
                return False
            
            left = helper(current.left, low, current.val)
            right = helper(current.right, current.val, high)

            return left and right
        
        return helper(root)
        