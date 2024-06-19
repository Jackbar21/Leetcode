# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     raise Exception("Not Reachable")
        
        # if root is leaf node
        if not root.left and not root.right:
            return root.val == 1
        
        # OR case
        if root.val == 2:
            if self.evaluateTree(root.left):
                return True
            return self.evaluateTree(root.right)
        
        # AND case
        if not self.evaluateTree(root.left):
            return False
        return self.evaluateTree(root.right)
        
