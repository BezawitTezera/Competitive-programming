class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        up = 0
        down = 0

        while up < len(nums1) and down < len(nums2):
            if nums1[up] < nums2[down]:
                up += 1
            elif nums1[up] > nums2[down]:
                down += 1
            else:
                return nums1[up]   
        
        return -1