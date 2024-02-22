class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1Counter = Counter(nums1)
        num2Counter = Counter(nums2)

        intersection = list((num1Counter & num2Counter).elements())
        return intersection