# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findpath(self, root, n):
        def recur(root, pos, n):
            if root == None:
                return None
            pos.append(root.val)
            if root.val == n:
                return pos[:]
                
            left = recur(root.left, pos, n)
            if left:
                return left
            right = recur(root.right, pos, n)
            if right:
                return right
            pos.remove(root.val)
            return None
        return recur(root, [], n) or []
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ppath = self.findpath(root, p.val)
        qpath = self.findpath(root, q.val)
        lca = None
        for i in ppath:
            for j in qpath:
                #print(str(i)+" "+str(j))
                if i == j:
                    lca = i
        def find_node(root, val):
            if not root:
                return None
            if root.val == val:
                return root
            return find_node(root.left, val) or find_node(root.right, val)

        return find_node(root, lca)
        
        return ans