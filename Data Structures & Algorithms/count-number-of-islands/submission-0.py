class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]
        count = 0
        visited = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(coordinate):
            x,y = coordinate
            if not (0<=x<m and 0<=y<n):
                return
            
            if grid[x][y]!="1":
                return 
            visited.add((x,y))
            for direction in directions:
                i,j = direction
                u,v = x+i,y+j
                if (u,v) not in visited:
                    dfs([u,v])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and ((i,j) not in visited):
                    count+=1
                    dfs([i,j])
        return count
        