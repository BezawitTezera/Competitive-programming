# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def current(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr
        if not root:
            return
        if key == root.val:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                temp = current(root.right)
                root.val = temp.val

                root.right = self.deleteNode(root.right, temp.val)

        elif key < root.val:
            root.left =  self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
       
        return root
        


        