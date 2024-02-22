class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)  
        product =1
        for i in range(1,len(nums)):
            result[i] = result[i -1 ]*nums[i-1]
        for i in range(len(nums) -1, -1, -1):
            result[i] *= product
            product *= nums[i]
        return result
