class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        nums.sort()
        def backtrack(index):
            if path not in ans:
                ans.append(path[:])

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return ans