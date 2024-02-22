class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        REQUIREMENT:
        INPUT : List of numbers, int-target
        RETURN: List of indices
        DATA STRUCTURE: Array
        ALGORITHM: Two Pointers
        TIME COMPLEXITY: O(nlogn)
        PSEUDOCODE:
        1. declare a variable left = 0
        2. declare a variable right = len(nums) - 1
        3. iterate while left < right
        4. declare sum_ = nums[left] + nums[right]
        5. if sum_ == target, return [left + 1, right + 1]
        6. elif sum_ < target, increment left
        7. else, decrement right
        8. return None out of the loop
"""
        left = 0
        right = len(numbers) - 1
        while left < right: 
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                return [left+1, right+1]
            elif sum_ < target:
                left += 1
            else:
                right -= 1
        return None
        