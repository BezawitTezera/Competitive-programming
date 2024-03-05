class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [1,2,3,4,5,6,7,8,9]
        ans = []
        path = []
        candidates.sort()
        def back(index):
            if len(path) == k:
                if sum(path) == n and path not in ans:
                    ans.append(path[:])
                    return
                elif sum(path) > n:
                    return
            
            for i in range(index, len(candidates)):
                path.append(candidates[i])
                back(i + 1)
                val = path.pop()
                
        if sum(candidates) >= n:
            back(0)
        return ans