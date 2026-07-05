class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    x = board[i][j]
                    rows[i].add(x)
                    cols[j].add(x)
                    boxes[(i//3)*3 + j//3].add(x)

        def dfs(pos):
            if pos == len(empty):
                return True

            i, j = empty[pos]
            b = (i//3)*3 + j//3

            for ch in "123456789":
                if ch not in rows[i] and ch not in cols[j] and ch not in boxes[b]:
                    board[i][j] = ch
                    rows[i].add(ch)
                    cols[j].add(ch)
                    boxes[b].add(ch)

                    if dfs(pos + 1):
                        return True

                    board[i][j] = "."
                    rows[i].remove(ch)
                    cols[j].remove(ch)
                    boxes[b].remove(ch)

            return False

        dfs(0)