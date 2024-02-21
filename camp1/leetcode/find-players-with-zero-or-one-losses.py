class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dictMatches = defaultdict(lambda: [0,0])
        ans = [[],[]]
        for match in matches:
            dictMatches[match[0]][0] += 1
            dictMatches[match[1]][1] += 1
        
        for key, value in dictMatches.items():
            if value[1] == 0:
                ans[0].append(key)
            elif value[1] == 1:
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans
