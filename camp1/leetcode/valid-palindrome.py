class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strings = ""
        for string in s:
            if string.isalpha():
                strings += string
            elif string.isdigit():
                strings += string
        strings = strings.lower()
        if strings[::] == strings[::-1]:
            return True
        else:
            return False
        