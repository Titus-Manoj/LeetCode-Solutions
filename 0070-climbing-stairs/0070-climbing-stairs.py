class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        while n>0:
            t = a+b
            a = b
            b = t
            n-=1
        return a
