class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mpp = {}
        for i, num in enumerate(nums):
            if num in mpp and i - mpp[num] <= k:
                return True
            mpp[num] = i
        return False