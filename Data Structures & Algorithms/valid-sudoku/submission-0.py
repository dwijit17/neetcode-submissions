class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            s = set()
            for ele in row:
                if (ele in s) and (ele!="."):
                    return False
                s.add(ele)
        
        for i in range(9):
            s = set()
            for j in range(9):
                ele = board[j][i]
                if (ele in s) and (ele!="."):
                    return False
                s.add(ele)
        check = [[set() for j in range(3)] for i in range(3)]
        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if (ele in check[i//3][j//3]) and (ele!="."):
                    return False
                check[i//3][j//3].add(ele)
        return True
        
