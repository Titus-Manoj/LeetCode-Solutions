import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for i in stones:
            heapq.heappush(hp, -i)
        while len(hp) > 1:
            n1 = -heapq.heappop(hp)
            n2 = -heapq.heappop(hp)

            if n1!=n2:
                heapq.heappush(hp, -abs(n1-n2))
        if len(hp) == 0:
            return 0
        return -heapq.heappop(hp)
