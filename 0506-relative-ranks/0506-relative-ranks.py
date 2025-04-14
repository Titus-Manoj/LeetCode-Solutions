import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hp = [-x for x in score]
        heapq.heapify(hp)
        d = {}
        n = len(score)
        ans = [""]*n
        pos = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        posn = 1

        
        
        for i in range(n):
            if score[i] not in d:
                d[score[i]] = i
        
        while hp:
            temp = -heapq.heappop(hp)
            index = d[temp]
            if posn == 1:
                ans[index] = pos[0]
            elif posn == 2:
                ans[index] = pos[1]
            elif posn == 3:
                ans[index] = pos[2]
            else:
                ans[index] = str(posn)
            posn += 1
        
        return ans