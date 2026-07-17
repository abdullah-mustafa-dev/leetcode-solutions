# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        def max_d(current):
            if current is None:
                return 0

            left = max_d(current.left)
            right = max_d(current.right)
            return 1 + max(left, right)
        return max_d(root)
        