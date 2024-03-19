class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        firstList.sort()
        secondList.sort()
        i = 0
        j = 0
        ans = []
        
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                ans.append([start, end])

            if firstList[i][1] > secondList[j][1]:
                j += 1

            else:
                i += 1

        return ans