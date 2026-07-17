# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.result = None
        self._inorder(root)
        return self.result

    def _inorder(self, node):
        if not node or self.result is not None:
            return
        self._inorder(node.left)
        if self.result is not None:
            return
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        self._inorder(node.right)
        