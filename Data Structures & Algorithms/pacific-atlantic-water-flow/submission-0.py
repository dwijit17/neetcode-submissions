class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        store = [[0]*n for i in range(m)]
        #think the water coming from the ocean to the land 
        #it can only travel in the increasing sequnce
        #whichever the cell had both water accumulated is the cell we put in answer
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]
        #mark all the top left cells as pacific
        #top
        queue = deque([])
        for i in range(n):
            store[0][i] |= 1
            queue.append((0,i))
        #left
        for j in range(1,m):
            store[j][0] |= 1
            queue.append((j,0))
        def bfs(bit):
            while queue:
                x,y = queue.popleft()
                for direction in directions:
                    i,j = direction
                    u,v = x+i,y+j
                    if 0<=u<m  and 0<=v<n and ((store[u][v] & bit == 0)and heights[u][v]>=heights[x][y]):
                        store[u][v] |= bit
                        queue.append((u,v))
        bfs(1)
        #down
        for i in range(n):
            store[m-1][i] |= 2
            queue.append((m-1,i))
        #right
        for j in range(m-1):
            store[j][-1] |= 2
            queue.append((j,n-1))
        bfs(2)
        ans = []
        for i in range(m):
            for j in range(n):
                if store[i][j]==3:
                    ans.append([i,j])

        return ans

        