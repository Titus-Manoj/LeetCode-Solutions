class Solution:
    def setZeroes(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col0 = 1
        for i in range(len(A)):
            if A[i][0] == 0:
                col0 = 0
            for j in range(1, len(A[0])):
                if A[i][j] == 0:
                    A[i][0] = 0
                    A[0][j] = 0
                
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                if A[i][0] == 0 or A[0][j] == 0:
                    A[i][j] = 0

        if A[0][0] == 0:
            for j in range(len(A[0])):
                A[0][j] = 0

        if col0 == 0:
            for i in range(len(A)):
                A[i][0] = 0
        

