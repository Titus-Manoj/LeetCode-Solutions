class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sun = nums[0]
        for i in range(1, len(nums)):
            sun ^= nums[i]
        return sun