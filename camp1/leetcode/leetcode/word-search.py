class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        row = len(board)
        col = len(board[0])

        def isValid(r, c):
            return 0 <= r < row and 0 <= c < col

        def backtrack(position, index):
            r, c = position

            if not isValid(r, c) or board[r][c] != word[index] or position in visited:
                return False

            if index == len(word) - 1:
                return True

            visited.add(position)

            distance = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in distance:
                new_r, new_c = r + x, c + y
                if backtrack((new_r, new_c), index + 1):
                    return True

            visited.discard(position)
            return False

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if backtrack((i, j), 0):
                        return True
        return False
