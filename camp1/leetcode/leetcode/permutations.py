class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        visited = set()
        def backtrack():
            if len(nums) == len(path):               
                ans.append(path[:])
                return

            for i in range(len(nums)):    
                if i not in visited:           
                    path.append(nums[i])
                    visited.add(i)
                    backtrack()
                    path.pop()
                    visited.remove(i)

        backtrack()
        return ans