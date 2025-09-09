class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sumr = 0
        ans = nums[0]
        for i in nums:
            if sumr+i>0:
                if sumr+i > ans:
                    ans = sumr+i
                sumr += i
        if sumr+i > ans:
            ans = sumr
        return ans
            