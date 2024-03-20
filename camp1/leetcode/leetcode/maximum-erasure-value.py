class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited = set()
        max_ = 0
        sum_ = 0

        i = 0
        for j in range(len(nums)):
            while nums[j] in visited:
                visited.remove(nums[i])
                sum_ -= nums[i]
                i += 1
            
            visited.add(nums[j])
            sum_ += nums[j]
            max_ = max(max_ , sum_)

        return max_
