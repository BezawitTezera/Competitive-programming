class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(len(bookings)):
            ans[bookings[i][0] - 1] += bookings[i][2]
            ans[bookings[i][1]] -= bookings[i][2]

        sum_ = 0
        for i in range(n + 1):
            sum_ += ans[i]
            ans[i] = sum_
            
        ans.pop()
        return ans