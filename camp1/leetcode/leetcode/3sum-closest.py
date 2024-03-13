class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        ans = 0
        min_ = float('inf')
        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == target:
                    return target
                elif nums[i] + nums[left] + nums[right] < target:
                    if abs(target - (nums[i] + nums[left] + nums[right])) < min_:
                        min_ = abs(target - (nums[i] + nums[left] + nums[right]))
                        ans = nums[i] + nums[left] + nums[right]
                    left += 1
                else:
                    if abs(target - (nums[i] + nums[left] + nums[right])) < min_:
                        min_ = abs(target - (nums[i] + nums[left] + nums[right]))
                        ans = nums[i] + nums[left] + nums[right]
                    right -= 1
        return ans
