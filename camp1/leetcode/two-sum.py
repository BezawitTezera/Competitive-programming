class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    index.append(i)
                    index.append(j)
                    return index

num = [3, 3]
target = 6
number = Solution()
print(number.twoSum(num, target))
