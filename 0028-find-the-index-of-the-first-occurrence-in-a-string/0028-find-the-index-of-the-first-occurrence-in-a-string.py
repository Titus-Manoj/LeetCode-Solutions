class Solution:
    def strStr(self, h: str, n: str) -> int:
        i, j = 0, 0
        pos = 0
        while(i<len(h)):
            j = 0
            if h[i] == n[j]:
                pos = i
                while(i<len(h) and j<len(n) and h[i] == n[j]):
                    i+=1
                    j+=1
                if j == len(n):
                    return pos
                else:
                    i = pos+1
            else:
                i+=1
        return -1