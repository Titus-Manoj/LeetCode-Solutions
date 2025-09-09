class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = []
        a = [1]
        ans.append(a)
        while(n-1):
            b = [1]
            for i in range(len(a)-1):
                b.append(a[i]+a[i+1])
            b.append(1)
            ans.append(b)
            a = b
            n -= 1
        return ans