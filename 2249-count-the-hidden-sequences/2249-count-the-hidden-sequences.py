class Solution:
    def numberOfArrays(self, dif: List[int], lower: int, upper: int) -> int:
        arr = [0]
        for i in range(len(dif)):
            temp = arr[i] + dif[i]
            arr.append(temp)
        
        u = upper - max(arr)
        l = lower - min(arr)

        return u - l + 1 if u>=l else 0