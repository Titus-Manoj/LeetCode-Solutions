# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        if root == None:
            return 0
        q = [(root, 1)]
        while(q):
            temp, height = q.pop(0)
            if temp.left == None and temp.right == None:
                return height
            if temp.left:
                q.append((temp.left, height + 1))
            if temp.right:
                q.append((temp.right, height + 1))
        return height
            
