class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        k = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j]) 
                k = (i // 3) * 3 + (j // 3)
                if board[i][j] in boxes[k]:
                    return False
                else: boxes[k].add(board[i][j])
        return True
