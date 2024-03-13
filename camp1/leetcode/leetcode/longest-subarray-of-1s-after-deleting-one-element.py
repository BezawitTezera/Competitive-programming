class Solution:
    def longestSubarray(self, nums: List[int]) -> int: 
        i = 0
        sum_ = max_ = 0
        for j in range(len(nums)):
            sum_ += nums[j]
            while (j - i + 1) - sum_ > 1:
                sum_ -= nums[i]
                i += 1
            max_ = max(max_, j - i)
        return max_
