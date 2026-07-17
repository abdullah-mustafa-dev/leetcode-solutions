# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        info = {}
        def walk(current, parent, depth):
            if not current:
                return

            if current.val == x or current.val == y:
                info[current.val] = (depth, parent)

            walk(current.left, current, depth + 1)
            walk(current.right, current, depth + 1)

        walk(root, None, 0)
        if x in info and y in info:
            x_depth, x_parent = info[x]
            y_depth, y_parent = info[y]
            return y_depth == x_depth and x_parent != y_parent
        return False