class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = 0
        sumArray = []
        for i in range(len(nums)):
            sums += nums[i]
            sumArray.append(sums)
        return sumArray
