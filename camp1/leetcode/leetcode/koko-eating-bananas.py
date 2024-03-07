class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 0
        high = max(piles)
        while low + 1 < high:
            count = 0
            mid = (low + high) // 2

            for pile in piles:
                count += ceil(pile/mid)
                
            if count <= h:
                high = mid
            else:
                low = mid
        return high