class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        finalAnswer = 0
        prev_value = 0  # Variable to hold the value of the previous symbol
        for char in s:
            current_value = roman_dict[char]

            if current_value > prev_value:
                finalAnswer += current_value - 2 * prev_value  # Subtract twice the previous value
            else:
                finalAnswer += current_value

            prev_value = current_value

        return finalAnswer

S = Solution()
print(S.romanToInt("III"))  # Output: 3
