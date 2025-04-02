class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans, maxdiff, maxelem = 0,0,0
        for i in nums:
            ans = max(ans, maxdiff*i)
            maxdiff = max(maxdiff, maxelem - i)
            maxelem = max(maxelem, i)
        return ans