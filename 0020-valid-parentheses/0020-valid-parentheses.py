class Solution:
    def isValid(self, s: str) -> bool:
        hp = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        stk = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stk.append(i)
            else:
                if stk:
                    temp = stk.pop()
                    if i != hp[temp]:
                        return False
                else:
                    return False
        
        if stk:
            return False
        
        return True
