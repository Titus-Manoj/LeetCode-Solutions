class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(lft, rgt, s):
            if lft == rgt and lft + rgt == n*2:
                res.append(s)
                return
            
            if lft < n:
                dfs(lft + 1, rgt, s + "(")
            
            if rgt < lft:
                dfs(lft, rgt+1, s + ")")
        
        dfs(0,0,"")
        return res