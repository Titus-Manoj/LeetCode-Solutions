class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        while n>0:
            b = a+b
            a = b-a
            #b = t
            n-=1
        return a
