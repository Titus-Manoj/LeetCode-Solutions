class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        m = {}
        for i in d.values():
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        
        for i in m.values():
            if i != 1:
                return False
        
        return True