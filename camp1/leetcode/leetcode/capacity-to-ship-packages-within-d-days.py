class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #take the sums            
        max_ = max(weights) - 1
        sum_ = sum(weights)
        def daycalc(capacity):
            packages = 0
            count = 0
            for num in weights:
                packages += num 
                if packages > capacity:
                    count += 1
                    packages = num
            return count + 1
        
        while max_ + 1 < sum_:
            mid = (max_ + sum_) // 2
            if daycalc(mid) <= days:
                sum_ = mid
            else:
                max_ = mid
        return sum_
        

            

