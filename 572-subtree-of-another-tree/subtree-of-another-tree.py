# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return not p and not q
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        # if self.isSameTree(root.left, subRoot):
        #     return True
        
        # if self.isSameTree(root.right, subRoot):
        #     return True
        if self.isSubtree(root.left, subRoot):
            return True
        
        if self.isSubtree(root.right, subRoot):
            return True
        
        return False

        

        