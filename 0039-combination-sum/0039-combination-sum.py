class Solution:
    def recur(self, ans, pos, add, target, cand, i):
        if add == target:
            ans.append(pos[:])
        elif add<target:
            for j in range(i, len(cand)):
                pos.append(cand[j])
                self.recur(ans, pos, add + cand[j], target, cand, j)
                pos.pop()
        return ans

    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        ans = []
        pos = []
        add = 0
        return self.recur(ans, pos, add, target, cand, 0)