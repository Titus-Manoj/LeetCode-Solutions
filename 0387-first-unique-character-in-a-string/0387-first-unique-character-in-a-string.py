class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = -1
        for i in range(len(s)):
            flg = 0
            for j in range(len(s)):
                if i!=j and s[i]==s[j]:
                    flg = 1
                    break
            if flg == 0:
                index = i
                break
        return index