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
        
        e1, e2 = self.evaluateTree(root.left), self.evaluateTree(root.right)
        return (e1 or e2) if root.val == 2 else (e1 and e2)
        
