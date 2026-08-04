# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        self.ans = 0
        def helper(current, curSum):
            if current and not current.left and not current.right:
                self.ans += curSum
            if not current:
                return
            
            leftSum = curSum * 10 + current.left.val if current.left else 0
            left = helper(current.left, leftSum)
            rightSum = curSum * 10 + current.right.val if current.right else 0
            right = helper(current.right, rightSum)
        
        helper(root, root.val)
        return self.ans