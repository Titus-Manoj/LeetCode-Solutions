class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        ans = 0
        i = 0

        for j in range(len(s)):
            if s[j] not in d:
                d[s[j]] = 1
            else:
                d[s[j]] += 1
            maxfrq = max(d.values())
            curr = j-i+1
            if curr - maxfrq > k:
                d[s[i]] -= 1
                i += 1
            ans = max(ans, j-i+1)
        
        return ans