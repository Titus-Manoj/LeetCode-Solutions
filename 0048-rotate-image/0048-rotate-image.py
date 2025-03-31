class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(m)):
            for j in range(i,len(m[0])):
                temp = m[i][j]
                m[i][j] = m[j][i]
                m[j][i] = temp
        
        for i in range(len(m)):
            m[i].reverse()
        
        return