import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k==0:
            return []

        ans = []
        hp = [] 

        for i in range(min(k, len(nums1))):
            heapq.heappush(hp, (nums1[i] + nums2[0], i, 0))
        
        while k>0 and hp:
            total, i, j = heapq.heappop(hp)
            ans.append([nums1[i], nums2[j]])

            if j+1 < len(nums2):
                heapq.heappush(hp, (nums1[i] + nums2[j+1], i, j+1))
            k-=1
        
        return ans