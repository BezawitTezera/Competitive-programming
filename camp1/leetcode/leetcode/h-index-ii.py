class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        size = len(citations)
        while left <= right:
            mid = (left + right) //2
            if size - mid == citations[mid]:
                return size - mid
            elif size - mid < citations[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return size - left

