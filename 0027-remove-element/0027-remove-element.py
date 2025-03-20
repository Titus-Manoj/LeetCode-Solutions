from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0  # Pointer for the next position to place a non-val element
        
        for i in range(len(nums)):  # Fast pointer
            if nums[i] != val:
                nums[j] = nums[i]  # Move non-val element to position j
                j += 1  # Increment position pointer
        
        return j  # New length of the modified array
