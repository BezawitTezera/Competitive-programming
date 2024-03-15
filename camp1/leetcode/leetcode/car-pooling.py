class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        max_ = max(trips[i][2] for i in range(len(trips)))
        ans = [0] * (max_ + 1)

        for i in range(len(trips)):
            ans[trips[i][1]] += trips[i][0]
            ans[trips[i][2]] -= trips[i][0]
        
        sum_ = 0

        for i in range(len(ans)):
            sum_ += ans[i]
            if sum_ > capacity:
                return False
            

        return True
