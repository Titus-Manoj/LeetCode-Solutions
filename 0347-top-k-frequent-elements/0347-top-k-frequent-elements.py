class Solution:
    def findMax(self, key: List[int], value: List[int]) -> int:
        maxx, index = 0, -1
        for i in range(len(value)):
            if value[i] >= maxx:
                maxx = value[i]
                index = i
        value[index] = 0
        return key[index]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        key = []
        value = []
        ele = nums[0]
        count = 1
        #Take case of nums = 1
        for i in range(1,len(nums)):
            if nums[i] == ele:
                count += 1
            else:
                key.append(ele)
                value.append(count)
                ele = nums[i]
                count = 1
        key.append(ele)
        value.append(count)
        ans = []
        while k!=0:
            ans.append(self.findMax(key, value))
            k -= 1
        return ans
