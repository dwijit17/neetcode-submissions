class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = (1<<31)-1
        queue = deque([])
        m = len(grid)
        n = len(grid[0])
        visited = set()
        #added the zeros to the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    queue.append((i,j,-1))
        #need to start the bfs from the zeros
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        
        while queue:
            x,y,dist = queue.popleft()
            if not (0<=x<m and 0<=y<n):
                continue
            #if its in range and not the inf
            if grid[x][y]==-1 or ((x,y) in visited):
                continue
            visited.add((x,y))
            grid[x][y] = dist+1
            #need to go all the directions
            for direction in directions:
                i,j = direction
                queue.append((x+i,y+j,grid[x][y]))
        


        
        