class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        square_set = [set() for _ in range(9)]

        rows = len(board)
        cols = len(board[0])

        for col in range(cols):
            for row in range(rows):
                current_cell = board[col][row]
                if current_cell != "." :
                    current_cell= int(current_cell)
                    # Let's add the current cell to the row set
                    if current_cell not in row_set[col]:
                        row_set[col].add(current_cell)
                    else:
                        return False

                    # Let's add the current cell to the col set
                    if current_cell not in col_set[row]:
                        col_set[row].add(current_cell)
                    else:
                        return False

                    square_index = (row // 3) + 3*(col// 3)

                    if current_cell not in square_set[square_index]:
                        square_set[square_index].add(current_cell)
                    else:
                        return False
                        
        return True 