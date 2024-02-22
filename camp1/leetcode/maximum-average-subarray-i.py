class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        REQUIREMENT:
        INPUT = list, int
        RETURN = float, .5f
        DATA STRUCTURE: list
        ALGORITHM: Sliding windows
        TIME CPOMPLECITY: O(N)
        SPACE COMPLEXITY: O(1)
        PSEUDOCODE:
        1. Declare variable i =0
        2. Declare variable sum_ = sum(nums[:k])
        3. declare max_ = sum_ / k
        4. iterate until i + k < len(nums)
        5.      average = float(f"{sum_/k: .5f}")
        6.      max_ = max(max_, average)
        7.      sum_ = sum - nums[i] + nums[i+k]
        8. average = float(f"{sum_/k: .5f}") #outside of loop
        9. max_ = max(max_, average)
        10. return max
        """
        i = 0
        sum_ = sum(nums[:k])
        max_ = sum_ / k
        while i + k < len(nums):
            average = sum_/k
            max_ = max(max_, average)
            sum_ = sum_ - nums[i] + nums[i+k]
            i+=1
        average = sum_ / k
        max_ = max(max_, average)
        return max_        