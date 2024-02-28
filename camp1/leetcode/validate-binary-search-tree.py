# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def traverse(root):
            if root == None:
                return
            traverse(root.left)
            ans.append(root.val)
            traverse(root.right)

        traverse(root)

        return len(set(ans)) == len(ans) and ans == sorted(ans)
