class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        pre = [0]*len(nums)
        post = [0]*len(nums)
        pre[0] = nums[0]
        for i in range(1,len(nums)):
            pre[i] = nums[i] + pre[i-1]
        post[0] = pre[len(nums)-1]
        for i in range(1,len(nums)):
            post[i] = post[i-1] - nums[i-1]
        if post[1] == 0:
            return 0
        for i in range(len(nums)):
            if pre[i] == post[i]:
                return i
        if pre[len(nums)-2] == 0:
            return len(nums)-1
        return -1
        