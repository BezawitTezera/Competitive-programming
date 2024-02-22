class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = [] 
        number = sorted(nums)
        for i in range(len(nums)):
            val = number.index(nums[i]) 
            ans.append(val)
        return ans