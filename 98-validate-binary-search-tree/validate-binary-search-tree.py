# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, -pow(2,31), pow(2,31) - 1)
    
    def isValid(self, root, lower_bound, upper_bound):
        if not root:
            return True
        
        if not (lower_bound <= root.val <= upper_bound):
            return False
        
        return (
            self.isValid(root.left, lower_bound, min(upper_bound, root.val - 1))
            and self.isValid(root.right, max(lower_bound, root.val + 1), upper_bound)
        )
