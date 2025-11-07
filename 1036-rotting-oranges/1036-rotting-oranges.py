from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # Step 1: Initialize queue and count fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        # If no fresh oranges, no time needed
        if fresh == 0:
            return 0

        # Directions: right, left, down, up
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes = 0

        # Step 2: BFS
        while q:
            size = len(q)
            new_rotted = False
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  # rot it
                        fresh -= 1
                        q.append((nx, ny))
                        new_rotted = True
            if new_rotted:
                minutes += 1

        # Step 3: Check if all fresh oranges rotted
        return minutes if fresh == 0 else -1
