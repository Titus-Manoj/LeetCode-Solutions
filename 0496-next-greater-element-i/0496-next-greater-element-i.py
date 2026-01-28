class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hp = defaultdict(lambda: -1)
        stk = []

        for i in reversed(nums2):
            while stk and stk[-1] <= i:
                stk.pop()
            hp[i] = -1 if not stk else stk[-1]
            stk.append(i)
        
        return [hp[num] for num in nums1]