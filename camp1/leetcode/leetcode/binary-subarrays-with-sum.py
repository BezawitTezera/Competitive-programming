class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        count = 0
        prefix_sum_counts = defaultdict(int)
        prefix_sum_counts[0] = 1 
        for num in nums:
            prefix_sum += num
           
            count += prefix_sum_counts[prefix_sum - goal]
            prefix_sum_counts[prefix_sum] += 1
        
        return count
