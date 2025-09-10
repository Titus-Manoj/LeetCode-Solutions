from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        
        # Step 1: find first decreasing element from right
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            # Step 2: find just larger element to the right
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: reverse suffix
        nums[i+1:] = reversed(nums[i+1:])
