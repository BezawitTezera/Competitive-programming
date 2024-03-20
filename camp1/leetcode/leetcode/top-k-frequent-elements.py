class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        sortedDictionary = sorted(counter.items(), key = lambda x: x[1], reverse = True)

        output = []
        for i in range(k):
            output.append(sortedDictionary[i][0])

        return output