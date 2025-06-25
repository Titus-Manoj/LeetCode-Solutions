from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        ans = []
        if root == None:
            return []
        q.append((root,0))
        add = 0
        count = 0
        currlvl = 0
        while q:
            node, lvl = q.popleft()
            if node == None:
                continue
            
            if lvl == currlvl:
                add += node.val
                count += 1
            else:
                ans.append(add/count)
                add = node.val
                count = 1
                currlvl += 1
            q.append((node.left, lvl+1))
            q.append((node.right, lvl+1))
        ans.append(add/count)
        return ans
            
