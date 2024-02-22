class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = []
        length = []
        for i in range(len(s)):
            if s[i] in substring:
                substring = substring[substring.index(s[i]) + 1:]
            substring.append(s[i])
            length.append(len(substring))
        return max(length) if length else 0
     
