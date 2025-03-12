class Solution:
    def countUnguarded(self, m: int, n: int, g: List[List[int]], w: List[List[int]]) -> int:
        arr = []
        for _ in range(m):
            row = [0]*n
            arr.append(row)
        
        for i in range(len(g)):
            arr[g[i][0]][g[i][1]] = 9
        
        for i in range(len(w)):
            arr[w[i][0]][w[i][1]] = 3
        
        for i in range(len(g)):
            r = g[i][0]
            c = g[i][1]
            for i in range(r+1, m):
                if arr[i][c] == 3:
                    break
                if arr[i][c] == 9:
                    break
                arr[i][c] = 1
            for i in range(r-1, -1,-1):
                if arr[i][c] == 3:
                    break
                if arr[i][c] == 9:
                    break
                arr[i][c] = 1
            for i in range(c+1, n):
                if arr[r][i] == 3:
                    break
                if arr[r][i] == 9:
                    break
                arr[r][i] = 1
            for i in range(c-1, -1,-1):
                if arr[r][i] == 3:
                    break
                if arr[r][i] == 9:
                    break
                arr[r][i] = 1
        count = 0
        for j in range(m):
            for k in range(n):
                if arr[j][k] == 0:
                    count += 1
        
        return count