class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for i in range(n)]
        ans = []
        def canplace(i,j,board):

            #shoulnt contain queen in that row
            if 'Q' in board[i]:
                return False
            
            #shouldnt contain queen in that col
            for k in range(n):
                if board[k][j]=='Q':
                    return False
            
            #shouldnt contain queen either diags
            #top left
            cpi,cpj = i,j
            while cpi>=0 and cpj>=0:
                if board[cpi][cpj]=="Q":
                    return False
                cpi-=1
                cpj-=1

            #top right
            cpi,cpj = i,j
            while cpi>=0 and cpj<n:
                if board[cpi][cpj]=="Q":
                    return False
                cpi-=1
                cpj+=1

            #bottom left
            cpi,cpj = i,j
            while cpi<n and cpj>=0:
                if board[cpi][cpj]=="Q":
                    return False
                cpi+=1
                cpj-=1

            #bottom right
            cpi,cpj = i,j
            while cpi<n and cpj<n:
                if board[cpi][cpj]=="Q":
                    return False
                cpi+=1
                cpj+=1
            return True
        
        def backtrack(board,currcol):
            if currcol==n:
                fans = []
                for row in board:
                    fans.append("".join(row))
                ans.append(fans)
                return 

            for i in range(n):
                if canplace(i,currcol,board):
                    board[i][currcol] = 'Q'
                    backtrack(board,currcol+1)
                    board[i][currcol] = '.'
                    
        backtrack(board,0)
        return ans