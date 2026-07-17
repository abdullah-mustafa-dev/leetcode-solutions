# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        def maximum(current):
            if not current:
                return 0

            left = max(maximum(current.left), 0)
            right = max(maximum(current.right), 0)

            self.max_sum = max(self.max_sum, current.val + left + right)

            return current.val + max(left, right)

        maximum(root)
        return self.max_sum
