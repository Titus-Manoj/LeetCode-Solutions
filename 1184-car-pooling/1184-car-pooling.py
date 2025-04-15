import heapq
class Solution:
    def carPooling(self, tp: List[List[int]], cap: int) -> bool:
        hp = []
        jr = [0]*1000
        for i in range(len(tp)):
            f, t, ppl = tp[i][1], tp[i][2], tp[i][0]
            for j in range(f-1, t-1):
                jr[j] += ppl
        
        for i in range(1000):
            if jr[i] > cap:
                return False
        return True
