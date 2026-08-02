class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Is Valid Columns
        for i in range(9):
            rows = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue

                if not 1 <= int(board[i][j]) <= 9:
                    return False

                if board[i][j] in rows:
                    return False

                rows.add(board[i][j])

        # Check columns
        for i in range(9):
            columns = set()
            for j in range(9):
                if board[j][i] == '.':
                    continue

                if not 1 <= int(board[j][i]) <= 9:
                    return False

                if board[j][i] in columns:
                    return False

                columns.add(board[j][i])

        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subBox = set()
                for ni in range(i, i + 3):
                    for nj in range(j, j + 3):
                        if board[ni][nj] == '.':
                            continue

                        if board[ni][nj] in subBox:
                            return False

                        subBox.add(board[ni][nj])

        return True