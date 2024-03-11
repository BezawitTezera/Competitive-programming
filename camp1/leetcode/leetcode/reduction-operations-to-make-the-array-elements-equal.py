class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        numSet = list(set(nums))
        numsCounter = Counter(nums)
        numSet.sort()
        count = 0

        for i in range(1,len(numSet)):
            count += i * numsCounter[numSet[i]]
        return count