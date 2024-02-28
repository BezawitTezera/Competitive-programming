# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check(root, p, q):
            if not root:
                return
            if root.val <= p.val and root.val >= q.val or root.val >= p.val and root.val <= q.val:
                return root           
            return check(root.left, p, q) or check(root.right, p, q)

        return check(root, p, q)