class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        start = nums[0]
        ans = []
        for i in range(len(nums)-1):
            if nums[i] + 1 != nums[i+1]:
                if start == nums[i]:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(nums[i]))
                start = nums[i+1]
        if start == nums[len(nums)-1]:
            ans.append(str(start))
        else:
            ans.append(str(start) + "->" + str(nums[len(nums)-1]))
        return ans
