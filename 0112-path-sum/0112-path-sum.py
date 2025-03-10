# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recur(node: Optional[TreeNode], curr_sum: int) -> bool:
            if not node:
                return False
            curr_sum += node.val
            if not node.left and not node.right and curr_sum == targetSum:
                return True
            return recur(node.left, curr_sum) or recur(node.right, curr_sum)
        
        return recur(root, 0)