import heapq
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        ans = [""] * n
        pos = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        posn = 1

        # Build max-heap with (score, index) pairs (negated score to simulate max-heap)
        hp = [(-score[i], i) for i in range(n)]
        heapq.heapify(hp)

        while hp:
            _, index = heapq.heappop(hp)
            if posn <= 3:
                ans[index] = pos[posn - 1]
            else:
                ans[index] = str(posn)
            posn += 1

        return ans
