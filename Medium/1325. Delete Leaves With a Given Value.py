# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def r(root):
            left,right = 0,0
            if root.left: left = r(root.left)
            if root.right: right = r(root.right)
            if root.left and left == 2: root.left = None
            if root.right and right == 2: root.right = None 
            return 2 if not root.left and not root.right and target == root.val else 1
        if r(root) == 2: return None
        return root
