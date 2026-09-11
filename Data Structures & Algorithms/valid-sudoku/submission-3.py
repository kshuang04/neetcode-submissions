class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRows():
            for i in range(9):
                seen = set()
                for j in range(9):
                    num = board[i][j]
                    if num == ".":
                        continue
                    
                    if num in seen:
                        return False
                    else:
                        seen.add(num)
            
            return True

        
        def checkCols():
            for i in range(9):
                seen = set()
                for j in range(9):
                    num = board[j][i]
                    if num == ".":
                        continue
                    
                    if num in seen:
                        return False
                    else:
                        seen.add(num)
            
            return True


        def checkBoxes():
            for box in range(9):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        r = (box // 3) * 3 + i
                        c = (box % 3) * 3 + j

                        num = board[r][c]
                        if num == ".":
                            continue

                        if num in seen:
                            return False
                        else:
                            seen.add(num)
            
            return True

                        
        return checkRows() and checkCols() and checkBoxes()