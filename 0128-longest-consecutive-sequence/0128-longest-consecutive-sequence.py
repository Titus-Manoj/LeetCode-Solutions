class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        hp = set(nums)

        for i in hp:
            if i-1 not in hp:
                cnt = 1
                while(i+cnt) in hp:
                    cnt += 1
                ans = max(ans, cnt)
        
        return ans
            