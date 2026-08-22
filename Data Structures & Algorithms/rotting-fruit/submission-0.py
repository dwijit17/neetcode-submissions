class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        m = len(grid)
        n = len(grid[0])
        #add the rotten oranges to the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j,0))
        
        #do the bfs from there
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        #need to find the total time required to make the all the oranges rotten
        ans = 0
        while queue:
            x,y,time = queue.popleft()
            ans = time
            for direction in directions:
                i,j = direction
                u,v = x+i,y+j
                if 0<=u<m and 0<=v<n and grid[u][v]==1:
                    grid[u][v] = 2
                    queue.append((u,v,time+1))
        
        #check if all the oranges became rotten otherwise return -1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return ans


        