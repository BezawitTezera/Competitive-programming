class NumArray:

    def __init__(self, nums: List[int]):
        self.nums= nums
        

    def sumRange(self, left: int, right: int) -> int:
        sum_ = 0
        ans = [0]
        for i in range(len(self.nums)):
            sum_ += self.nums[i]
            ans.append(sum_)
        return ans[right + 1] - ans[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)