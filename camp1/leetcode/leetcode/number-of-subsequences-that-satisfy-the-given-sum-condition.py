class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        sum_ = 0
        nums.sort()
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                sum_ += pow(2, right - left)
                left += 1
        return sum_ % (10**9 + 7)
                