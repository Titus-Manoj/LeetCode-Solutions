class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        if dp[0] == 0 and n>1:
            return False
        for i in range(1, n-1):
            dp[i] = max(dp[i-1]-1, nums[i])
            if dp[i] >= len(nums) - i - 1:
                return True
            if dp[i] == 0:
                return False
        
        return True
