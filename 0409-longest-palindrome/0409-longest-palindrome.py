class Solution:
    def longestPalindrome(self, s: str) -> int:
        sett = set()
        count = 0

        for i in s:
            if i in sett:
                sett.remove(i)
                count += 2
            else:
                sett.add(i)
        
        if sett:
            count += 1
        
        return count