class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.checkRows(board) and self.checkCols(board) and self.checkSubBoxes(board):
            return True
        else:
            return False

    def checkRows(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] is ".":
                    continue
                
                if board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
            
        return True

    def checkCols(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] is ".":
                    continue
                
                if board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])

        return True

    def checkSubBoxes(self, board: List[List[str]]) -> bool:
        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (box // 3) * 3 + i
                    col = (box % 3) * 3 + j
                    if board[row][col] is ".":
                        continue
                    
                    if board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        
        return True
