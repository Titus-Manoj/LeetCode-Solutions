class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxelem, maxdiff, ans = 0,0,0
        for i in nums:
            ans = max(maxdiff*i, ans)
            maxdiff = max(maxelem-i, maxdiff)
            maxelem = max(maxelem, i)
        return ans
