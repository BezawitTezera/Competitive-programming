class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        middleIndex = 0
        for i in range(len(nums)):
            if middleIndex == sum_ - nums[i] - middleIndex:
                return i
            middleIndex += nums[i]
        return -1