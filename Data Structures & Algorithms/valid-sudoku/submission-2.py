class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows():
            for i in range(9):
                seen = set()
                for j in range(9):
                    if board[i][j] == ".":
                        continue
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
            
            return True

        def checkCols():
            for i in range(9):
                seen = set()
                for j in range(9):
                    if board[j][i] == ".":
                        continue
                    if board[j][i] in seen:
                        return False
                    else:
                        seen.add(board[j][i])
            
            return True
        
        def checkBoxes():
            for box in range(9):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        row = (box // 3) * 3 + i
                        col = (box % 3) * 3 + j
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in seen:
                            return False
                        else:
                            seen.add(board[row][col])
            
            return True

        return checkRows() and checkCols() and checkBoxes()