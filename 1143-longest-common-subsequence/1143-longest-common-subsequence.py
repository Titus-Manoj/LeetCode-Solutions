class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        dp = [[0 for _ in range(len(t2)+1)] for _ in range(len(t1)+1)]
        
        for i in range(1, len(t1)+1):
            for j in range(1, len(t2)+1):
                if t1[i-1] == t2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]