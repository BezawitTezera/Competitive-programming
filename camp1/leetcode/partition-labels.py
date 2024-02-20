class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        ans = []
        last_occurance = {s[i]: i for i in range(n)}
        current = 0
        while current < n:
            end = last_occurance[s[current]]
            j = current + 1
            while j < end:
                end = max(end, last_occurance[s[j]])
                j += 1
            ans.append(end - current + 1)
            current = end + 1
        return ans
        