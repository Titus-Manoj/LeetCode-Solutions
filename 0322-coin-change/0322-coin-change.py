class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:
        dp = [amt+1] * (amt+1)
        dp[0] = 0

        for a in range(1, amt+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[-1] if dp[-1] != amt + 1 else -1