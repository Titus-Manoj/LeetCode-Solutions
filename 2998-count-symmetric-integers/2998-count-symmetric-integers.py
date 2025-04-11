class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            s = str(num)
            n = len(s)
            if n%2 == 0:
                first = s[:n//2]
                last = s[n//2:]
                sumf = 0
                suml = 0
                for i in range(n//2):
                    sumf += int(first[i])
                    suml += int(last[i])
                if sumf == suml:
                    count += 1
        return count