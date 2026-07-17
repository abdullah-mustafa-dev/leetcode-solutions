# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestUnivaluePath(self, root):
        self.longest = 0
        def helper(node):
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)

            left_path = 1 + left if node.left and node.left.val == node.val else 0
            right_path = 1 + right if node.right and node.right.val == node.val else 0

            self.longest = max(self.longest, left_path + right_path)

            return max(left_path, right_path)
        helper(root)
        return self.longest
        