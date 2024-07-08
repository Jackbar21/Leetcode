# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1, []) == self.getLeaves(root2, [])
    
    def getLeaves(self, root, acc):
        if not root:
            return acc
        
        self.getLeaves(root.left, acc)
        if not root.left and not root.right:
            acc.append(root.val)
        self.getLeaves(root.right, acc)

        return acc
