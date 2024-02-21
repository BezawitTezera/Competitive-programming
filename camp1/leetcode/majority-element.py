class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number = None
        count = 0
        for num in nums:
            if count == 0:
                number = num
            if num == number:
                count += 1
            else:
                count -=1 
        return number