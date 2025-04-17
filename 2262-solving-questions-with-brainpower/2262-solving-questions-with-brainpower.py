class Solution:
    def mostPoints(self, qs: List[List[int]]) -> int:
        n = len(qs)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, skip = qs[i][0], qs[i][1]
            next_i = i + skip + 1
            take = points + (dp[next_i] if next_i < n else 0)
            dont_take = dp[i + 1]
            dp[i] = max(take, dont_take)

        return dp[0]
