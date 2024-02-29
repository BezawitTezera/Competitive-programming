# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else 0
        
        level = height(root)
        
        def eachLevel(root, l):
            ans = []
            if not root:
                return []
            
            elif l == 1:
                ans.append(root.val)
            elif l > 1:
                ans.extend(eachLevel(root.left, l - 1))
                ans.extend(eachLevel(root.right, l - 1))
            return ans
        ans = []
        for i in range(1, level + 1):                 
            ans.append(eachLevel(root, i))
        
        for i in range(len(ans)):
            if i % 2!= 0:
                ans[i] = ans[i][::-1]
        return ans
            
           
