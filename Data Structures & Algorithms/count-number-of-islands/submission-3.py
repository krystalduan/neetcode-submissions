class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        def bfs(row, col): 
            queue = deque()
            queue.append((row,col))
            directions = [[0,1], [0,-1], [1,0], [-1,0]]
            while queue: 
                r, c = queue.popleft()
                visited.add((r,c))
                for d in directions: 
                    nr = r + d[0]
                    nc = c + d[1]
                    if nr <= len(grid)-1 and nc <= len(grid[0])-1 and nr >= 0 and nc >= 0 and (nr, nc) not in visited and grid[nr][nc] == "1" :
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited: 
                    bfs(row, col)
                    print(row,col)
                    islands += 1

        return islands



        