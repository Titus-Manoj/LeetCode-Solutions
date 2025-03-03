from typing import List

class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        # Step 1: Build adjacency list
        d = {i: [] for i in range(num)}  # Ensure all courses are present
        for course, prerequisite in pre:
            d[course].append(prerequisite)  # Reverse dependency mapping

        # Step 2: Use a visited list to track states
        visited = [0] * num  # 0 = Unvisited, 1 = Visiting, 2 = Visited
        
        # Step 3: DFS function to detect cycles
        def dfs(course):
            if visited[course] == 1:  # Cycle detected
                return True
            if visited[course] == 2:  # Already checked, no cycle
                return False
            
            visited[course] = 1  # Mark as visiting
            
            for prereq in d[course]:  # Check prerequisites
                if dfs(prereq):  # If a cycle is found
                    return True

            visited[course] = 2  # Mark as fully processed
            return False

        # Step 4: Run DFS for each course
        for i in range(num):
            if visited[i] == 0:  # If unvisited, start DFS
                if dfs(i):
                    return False  # Cycle detected

        return True  # No cycles found
