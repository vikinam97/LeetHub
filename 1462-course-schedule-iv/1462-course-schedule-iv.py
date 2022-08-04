class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        grid = [[float('inf')] * numCourses for i in range(numCourses)]
        
        for i in range(numCourses):
            grid[i][i] = 0
        
        for a, b in prerequisites:
            grid[a][b] = 1
            
        for pivot in range(numCourses):
            
            for i in range(numCourses):
                for j in range(numCourses):
                    if i==j or i == pivot or j == pivot:
                        continue
                    grid[i][j] = min(grid[i][j], grid[i][pivot] + grid[pivot][j])
        
        results = []
        
        for a, b in queries:
            results.append(grid[a][b] != float('inf'))
        
        return results
        