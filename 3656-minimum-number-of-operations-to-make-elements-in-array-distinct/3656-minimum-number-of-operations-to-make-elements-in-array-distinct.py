class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d = set()
        pos = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] in d:
                pos = i+1
                break
            else:
                d.add(nums[i])
        if pos != -1:
            if pos %3 == 0:
                return pos // 3
            else:
                return pos // 3 + 1
        
        return 0
        
