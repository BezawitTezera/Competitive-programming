class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        tasks.sort(key = lambda task: task[1] - task[0], reverse = True)
        ans = 0
        curr = 0
        for task in tasks:
            if curr <= task[1]:
                ans += task[1] - curr
            curr = max(curr - task[0], task[1] - task[0])
        return ans