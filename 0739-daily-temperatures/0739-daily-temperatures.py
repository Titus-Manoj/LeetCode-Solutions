class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stk = []
        ans = [0 for i in range(len(temp))]
        for i in range(len(temp)-1, -1, -1):
            while stk:
                #print(stk[-1])
                #print(temp[i])
                if temp[i] < stk[-1][0]:
                    ans[i] = stk[-1][1] - i
                    break
                else:
                    stk.pop()
            stk.append((temp[i], i))
            #print(stk[-1])
        
        return ans
