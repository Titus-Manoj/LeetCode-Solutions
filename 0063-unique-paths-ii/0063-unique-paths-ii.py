class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        if g[0][0] == 1:
            return 0
        dp = [[0 for _ in range(len(g[0]))] for _ in range(len(g))]
        dp[0][0] = 1
        
        for i in range(1, len(g)):
            if g[i][0] != 1:
                dp[i][0] = dp[i-1][0]

        for j in range(1, len(g[0])):
            if g[0][j] != 1:
                dp[0][j] = dp[0][j-1]

        for i in range(1, len(g)):
            for j in range(1, len(g[0])):
                if g[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]