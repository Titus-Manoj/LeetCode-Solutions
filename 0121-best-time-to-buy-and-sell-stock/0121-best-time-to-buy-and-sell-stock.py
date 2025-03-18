class Solution:
    def maxProfit(self, p: List[int]) -> int:
        minn = p[0]
        ans = 0
        for i in range(1, len(p)):
            if p[i]<minn:
                minn = p[i]
                continue
            ans = max(ans, p[i]-minn)
        return ans