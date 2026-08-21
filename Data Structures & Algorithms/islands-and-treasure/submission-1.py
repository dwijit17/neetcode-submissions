class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = (1<<31)-1
        queue = deque([])
        m = len(grid)
        n = len(grid[0])
        #added the zeros to the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    queue.append((i,j,0))
        #need to start the bfs from the zeros
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        
        while queue:
            x,y,dist = queue.popleft()     
            #need to go all the directions
            for direction in directions:
                i,j = direction
                u,v = x+i,y+j
                if 0<=u<m and 0<=v<n and grid[u][v]==inf:
                    grid[u][v] = dist+1
                    queue.append((u,v,dist+1))



        
        