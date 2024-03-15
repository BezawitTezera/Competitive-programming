class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = prod(nums)
        ans = []

        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(int(mult/nums[i]))
            else:
                if i != len(nums):
                    ans.append(int(prod(nums[:i]) * prod(nums[i + 1:])))
                else:
                    ans.append(mult)

        return ans