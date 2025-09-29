class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hp = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in hp:
                return [hp[diff], idx]  # return indices
            hp[num] = idx  # store number with its index
        return []