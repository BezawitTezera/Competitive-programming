class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        row = len(mat)
        col = len(mat[0])
        d = {}
        for i in range(row):
            for j in range(col):
                if i + j in d:
                    d[i+j].append(mat[i][j])
                else:
                    d[i+j] = [mat[i][j]]
        for key, value in d.items():
            if key % 2 == 0:
                value.reverse()
                ans.extend(value)
            else:
                ans.extend(value)
        return ans