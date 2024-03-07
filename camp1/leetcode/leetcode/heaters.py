class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        min_ = -1
        max_ = max(max(heaters), max(houses))

        while min_ + 1< max_:
            mid = (min_ + max_) // 2
            house = 0
            heater = 0
            while heater < len(heaters) and house < len(houses):
                if abs(heaters[heater] - houses[house] )> mid:
                    heater += 1
                else:
                    house += 1
            if  house == len(houses) and heater < len(heaters):
                ans = mid
                max_ = mid
            else:
                min_ = mid
                

        return ans