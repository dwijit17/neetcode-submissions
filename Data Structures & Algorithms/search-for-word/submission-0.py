class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()
        ans = [False]
        def helper(k,loop,i,j):
            # print("call",i,j)
            if k==len(word):
                ans[0] = True
                return
            if not loop:
                #checking over four directions
                #left
                if j-1>=0 and board[i][j-1]==word[k] and ((i,j-1) not in visited):
                    visited.add((i,j-1))
                    helper(k+1,False,i,j-1)
                    visited.remove((i,j-1))
                #right
                if j+1<n and board[i][j+1]==word[k] and ((i,j+1) not in visited):
                    visited.add((i,j+1))
                    helper(k+1,False,i,j+1)
                    visited.remove((i,j+1))
                
                #top
                if i-1>=0 and board[i-1][j]==word[k] and ((i-1,j) not in visited):
                    visited.add((i-1,j))
                    helper(k+1,False,i-1,j)
                    visited.remove((i-1,j))
                
                #bottom
                if i+1<m and board[i+1][j]==word[k] and ((i+1,j) not in visited):
                    visited.add((i+1,j))
                    helper(k+1,False,i+1,j)
                    visited.remove((i+1,j))

                return 

            for p in range(m):
                for q in range(n):
                    if ans[0]:
                        return 
                    ch = board[p][q]
                    if ch==word[k]:
                        #need to check over four directions
                        visited.add((p,q))
                        helper(k+1,False,p,q)
                        visited.remove((p,q))
        helper(0,True,None,None)
        return ans[0]

    
        