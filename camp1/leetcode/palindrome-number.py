class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        return x_str[::] == x_str[::-1]


num1 = 121
num = Solution()
print(num.isPalindrome(num1))