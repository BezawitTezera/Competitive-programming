class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        sum_ = 0
        min_ = float('inf')
        for j in range(len(nums)):
            sum_ += nums[j]
            while sum_ >= target:
                min_ = min(min_, j - i + 1)
                sum_ -= nums[i]
                i += 1
        return min_ if min_ != float('inf') else 0
