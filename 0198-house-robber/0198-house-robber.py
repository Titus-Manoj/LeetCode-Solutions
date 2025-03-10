class Solution:
    def rob(self, nums: List[int]) -> int:
        def rec(idx: int, dp: List[int]) -> int:
            if idx == 0:
                return nums[0]
            if idx == 1:
                return max(nums[0], nums[1])
            if dp[idx] != -1:
                return dp[idx]

            dp[idx] = max(nums[idx] + rec(idx - 2, dp), rec(idx - 1, dp))
            return dp[idx]

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [-1] * n
        return rec(n - 1, dp)