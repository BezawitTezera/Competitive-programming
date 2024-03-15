class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = defaultdict(int)

        count = 0
        sum_ = 0
        store[0] = 1

        for num in nums:
            sum_ += num

            if sum_ - k in store:
                count += store[sum_ - k]
            
            store[sum_] += 1

        return count