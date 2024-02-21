class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans = set()
        for i in range(len(ranges)):
            ans.update({num for num in range(ranges[i][0], ranges[i][1] + 1) })
        for i in range(left, right+1):
            if i not in ans:
                return False
        return True


        