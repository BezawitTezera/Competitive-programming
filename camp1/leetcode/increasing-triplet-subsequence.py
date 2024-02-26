class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num > second:
                return True
            elif num > first:
                second = min(num, second)
            first = min(num, first)
        return False