class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        ans = [0] * n
        count = 0
        max_index = 0

        for i in range(n):
            ans[flips[i] - 1] = 1
            max_index = max(max_index, flips[i])

            if max_index == i + 1 and sum(ans[:max_index]) == max_index:
                count += 1

        return count
