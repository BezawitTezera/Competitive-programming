# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(int)
        def traverse(root):
            if root == None:
                return
            traverse(root.left)
            ans[root.val] += 1
            traverse(root.right)
        
        traverse(root)
        val = []
        max_ = max(ans.values())
        for key, value in ans.items():
            if value == max_:
                val.append(key)
        return val