class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        value = bisect_left(arr, x)
        left, right = value - 1, value

        while k > 0:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
            k -= 1
        
        return arr[left + 1: right]
