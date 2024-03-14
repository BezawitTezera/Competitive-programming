class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        max_ = 0
        count = 0
        def checker(letter):
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return letter in vowels

        for j in range(len(s)):
            while j - i >= k:
                if checker(s[i]):
                    count -= 1
                i += 1
            if checker(s[j]):
                count += 1
            max_ = max(count, max_)
        return max_
                

