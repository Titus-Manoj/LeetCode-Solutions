class Solution:
    def searchMatrix(self, m: List[List[int]], trgt: int) -> bool:
        flg = 0
        i = 0
        j = len(m[0])-1
        while(i<len(m) and j>=0):
            if trgt > m[i][j] and flg == 0:
                i += 1
            elif trgt < m[i][j]:
                j -= 1 
                flg = 1   
            elif trgt == m[i][j]:
                return True
            else:
                break
        
        return False