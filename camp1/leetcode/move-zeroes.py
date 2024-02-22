class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        REQUIREMENT
        INPUT: Array
        RETURN: Array
        DATA STRUCTURE: Array
        ALGORITHM: Two pointer
        COMPLEXITY: 
        TIME COMPLEXITY: O(n)
        SPACE COMPLEXITY = O(1)
        PSEUDOCODE:
        1. create a function called Values with nums parenthesis
        2. Declare index = 0
        3. loop through all elements
        4. if nums is different 0
        5. swap, and increament index += 1
        6. return nums
        """
        index = 0
        for i in range(len(nums)):
            if nums[i]!= 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        return nums