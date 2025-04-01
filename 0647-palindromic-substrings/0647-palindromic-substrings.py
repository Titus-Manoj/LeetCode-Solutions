class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0

        def palin(l, r):
            count = 0
            while l>=0 and r<n and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            return count
        
        for i in range(n):
            even = palin(i, i+1)
            odd = palin(i, i)
            ans += even + odd
        
        return ans