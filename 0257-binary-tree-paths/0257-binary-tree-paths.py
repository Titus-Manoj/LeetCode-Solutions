# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        p = []
        self.recur(root, p, ans)
        return ans
    
    def recur(self, root, p, ans):
        if root==None:
            return
        p.append(root.val)
        if root.left==None and root.right==None:
            ans.append('->'.join(str(x) for x in p))
            p.pop()
            return
        self.recur(root.left, p, ans)
        self.recur(root.right, p, ans)
        p.pop()
        return
        