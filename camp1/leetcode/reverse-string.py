class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        REQUIREMENTS:
        1. Input = list
        2. return  = a list
        Complexity:
        Space complexity = o(1)
        Time = o(N)
        Pseudocode:
        1. using the built in python slicing method
        """
        s[::] = s[::-1]
        return s