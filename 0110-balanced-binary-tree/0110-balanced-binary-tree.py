# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findhth(self, node):
        if node is None:
            return 0
        return max(self.findhth(node.left), self.findhth(node.right)) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:  # Fix: Handle the case where root is None
            return True
        
        lft = self.findhth(root.left)
        rht = self.findhth(root.right)
        
        # Fix: Return a boolean instead of 0/1
        return abs(lft - rht) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)