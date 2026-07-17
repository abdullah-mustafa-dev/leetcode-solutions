# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        def sumOfLeftLeaves(self, root):
            def left_sum(current):
                if not current.left and not current.right:
                    return 0     

                left = 0
                if current.left:
                    if not current.left.left and not current.left.right:
                        left = current.left.val
                    else:
                        left = left_sum(current.left)
                right = left_sum(current.right) if current.right else 0

                return left + right

            return left_sum(root)
