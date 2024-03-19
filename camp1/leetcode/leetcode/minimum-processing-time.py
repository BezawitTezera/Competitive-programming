class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse = True)
        tasks.sort()
        max_ = float('-inf')
        i = 3
        for time in processorTime:
            max_ = max(max_, time + tasks[i])
            i += 4
        return max_