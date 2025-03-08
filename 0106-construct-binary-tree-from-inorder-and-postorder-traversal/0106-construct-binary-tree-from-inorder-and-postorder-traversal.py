# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, A: List[int], B: List[int]) -> Optional[TreeNode]:
        if not A or not B:
            return None
        root = TreeNode(B.pop())
        i = A.index(root.val)
        root.right = self.buildTree(A[i+1:],B)
        root.left = self.buildTree(A[:i],B)
        return root