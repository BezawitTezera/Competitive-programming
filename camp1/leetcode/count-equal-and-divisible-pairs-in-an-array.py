class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            if nums[left] == nums[right] and (left * right) % k == 0:
                print(left, right)
                count += 1
            right -= 1
            if right == left:
                left += 1
                right = len(nums) - 1

        return count