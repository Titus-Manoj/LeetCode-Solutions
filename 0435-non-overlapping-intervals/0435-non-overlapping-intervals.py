class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intval = sorted(intervals, key=lambda x: x[1])
        start = intval[0][0]
        end = intval[0][1]
        count = 0
        for i in range(1, len(intval)):
            if intval[i][0] < end:
                count += 1
            else:
                end = intval[i][1]
        return count