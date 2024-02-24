class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # ans = [[0]*len(strs[0])]* len(strs)
        val = []
        count = 0
        for i in range(len(strs[0])):
            ans = ""
            for j in range(len(strs)):
                ans += strs[j][i]
            val.append(ans)
        del ans

        for i in range(len(val)):
            sortedVal = ''.join(sorted(val[i]))
            if sortedVal != val[i]:
                count += 1
        return count