class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        # Step 1: Compute prefix products in ans[]
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]

        # Step 2: Compute suffix products on the fly and update ans[]
        suff = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suff
            suff *= nums[i]  # Update suffix product

        return ans