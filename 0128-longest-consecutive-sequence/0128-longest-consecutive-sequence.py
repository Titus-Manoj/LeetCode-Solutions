class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        maxx = 0
        for i in sett:
            if i-1 not in sett:
                count = 0
                while i + count in sett:
                    count+=1
                maxx = max(count, maxx)
        return maxx