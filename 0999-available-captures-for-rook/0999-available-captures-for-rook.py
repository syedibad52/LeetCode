class Solution:
    def numRookCaptures(self, board):
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    r, c = i, j

        ans = 0

        for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
            i, j = r, c
            while True:
                i += x
                j += y

                if i < 0 or i >= 8 or j < 0 or j >= 8:
                    break
                if board[i][j] == "B":
                    break
                if board[i][j] == "p":
                    ans += 1
                    break

        return ans