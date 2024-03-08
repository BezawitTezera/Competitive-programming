class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sum_ = 0
        count = 0
        for cost in costs:
            sum_ += cost
            if sum_ <= coins:
                count += 1


        return count 