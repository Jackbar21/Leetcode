# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.is_balanced = True
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.getHeightAndUpdateRes(root)
        return self.is_balanced

    def getHeightAndUpdateRes(self, root):
        # If self.is_balanced is False, then end execution context
        # as quickly as possible since answer will be False no matter what.
        if not root:
            return 0
        
        left_height = self.getHeightAndUpdateRes(root.left)
        right_height = self.getHeightAndUpdateRes(root.right)
        diff = abs(left_height - right_height)
        if diff > 1:
            self.is_balanced = False

        return 1 + max(left_height, right_height)
