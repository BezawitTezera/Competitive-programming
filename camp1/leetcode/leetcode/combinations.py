class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def helper(index, path):
            if len(path) == k:
                ans.append(path[:])
                return
            
            for i in range(index, n + 1):
                path.append(i)
                helper(i + 1, path)
                path.pop()
        helper(1, path)
        return ans
                
        