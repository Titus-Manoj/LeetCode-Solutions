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

        if n == 1:
            ans[0] = "Gold Medal"
            return ans
        if n == 2:
            maxx = max(score[0], score[1])
            if score[0] == maxx:
                ans[0] = "Gold Medal"
                ans[1] = "Silver Medal"
            else:
                ans[1] = "Gold Medal"
                ans[0] = "Silver Medal"
            return ans
        
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