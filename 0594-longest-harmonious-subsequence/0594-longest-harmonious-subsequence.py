class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        ans = 0
        for i in d:
            if i+1 in d:
                ans = max(ans, d[i] + d[i+1])
        
        return ans