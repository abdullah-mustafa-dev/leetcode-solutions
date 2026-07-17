# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def height(current):
            if not current:
                return 0

            left_height = height(current.left)
            right_height = height(current.right)

            self.diameter = max(self.diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)
        return self.diameter