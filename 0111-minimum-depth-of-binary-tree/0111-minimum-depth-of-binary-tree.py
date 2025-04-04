# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left = 2**31 - 1
        right = 2**31 - 1
        if root.left == None and root.right == None:
            return 1
        if root.left:
            left = self.minDepth(root.left) + 1
        if root.right:
            right = self.minDepth(root.right) + 1
        return min(left, right)