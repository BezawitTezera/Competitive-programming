class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in range(len(digits)):
            string += str(digits[i])
        nums = int(string) + 1
        val = str(nums)
        return [int(val[i]) for i in range(len(val))]