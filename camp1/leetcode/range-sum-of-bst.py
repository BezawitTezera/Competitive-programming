# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_ = 0
        if not root:
            return 0
        elif low <= root.val <= high:
            sum_ += root.val
        return self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high) + sum_
