class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        row = len(mat)
        column = len(mat[0])
        sum_ = 0
        for i in range(row):
            for j in range(column):
                if i == j:
                    sum_ += mat[i][j]
                elif i + j == row - 1:
                    sum_ += mat[i][j]
        return sum_