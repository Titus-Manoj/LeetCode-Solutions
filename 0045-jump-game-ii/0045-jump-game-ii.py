class Solution:
    def jump(self, nums: List[int]) -> int:
        x = float('inf')
        dp = [x for _ in range(len(nums))]
        dp[0] = 0
        
        for i in range(len(dp)):
            n = nums[i]
            j = 0
            while j<n and i+j+1<len(nums) and n>0:
                dp[i+j+1] = min(dp[i+j+1], 1 + dp[i])
                j += 1
        
        return dp[-1]
