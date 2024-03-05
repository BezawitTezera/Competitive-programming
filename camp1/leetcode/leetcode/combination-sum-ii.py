class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()
        def back(index):
            if sum(path) == target and path not in ans:
                ans.append(path[:])
                return
            elif sum(path) > target:
                return
            
            k = 0
            for i in range(index, len(candidates)):
                if k == candidates[i]:
                    continue
                path.append(candidates[i])
                back(i + 1)
                k = path.pop()
                
        if sum(candidates) >= target:
            back(0)
        return ans