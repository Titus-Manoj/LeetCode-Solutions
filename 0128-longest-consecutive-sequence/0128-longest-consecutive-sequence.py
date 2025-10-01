class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a, res, t = list(set(nums)), 0, 0
        heapq.heapify(a)
		
        while a:
            pop_val = heapq.heappop(a)
            t += 1
            if a == [] or a[0] != pop_val + 1:
                res = max(t, res)
                t = 0
        return res
            