class NumArray:

    def __init__(self, nums: List[int]):
        self.a = nums
        for i in range(1, len(self.a)):
            self.a[i] += self.a[i-1]
        return

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            ans = self.a[right]
        else:
            ans = self.a[right] - self.a[left-1]
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)