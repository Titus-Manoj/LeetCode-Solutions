class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rgt = [0 for i in range(len(nums))]
        rsum = 0
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                rgt[i] = nums[i]
            else:
                rgt[i] = rgt[i+1] + nums[i]
        lsum = 0
        for i in range(len(nums)):
            lsum += nums[i]
            if lsum == rgt[i]:
                return i
            
        
        return -1