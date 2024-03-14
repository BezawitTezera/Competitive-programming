class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        sum_ = max_ = 0
        for j in range(len(nums)):
            sum_ += nums[j]
            while (j - i + 1) - sum_ > k:
                sum_ -= nums[i]
                i += 1
            max_ = max(max_, j - i + 1)
        return max_
