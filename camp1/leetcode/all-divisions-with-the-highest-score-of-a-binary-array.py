class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = sum(nums)
        zeros = 0
        score = [ones]
        ans = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                ones -= 1
            score.append(zeros + ones)
        max_ = max(score)
        for i in range(len(score)):
            if score[i] == max_:
                ans.append(i)
        return ans
