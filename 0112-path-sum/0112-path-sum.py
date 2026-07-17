# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):

        def func(current, cur_sum=0):
            if not current:
                return False
            
            cur_sum += current.val
            
            if not current.left and not current.right:
                return cur_sum == targetSum

            return func(current.left, cur_sum) or func(current.right, cur_sum)

        return func(root)