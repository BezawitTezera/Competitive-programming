class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        even = [value for value in counter.values() if value % 2 == 0]
        odd = [value for value in counter.values() if value % 2 != 0]

        if odd:
            return sum(odd) - len(odd) + 1 + sum(even)
        else:
            return sum(even)
