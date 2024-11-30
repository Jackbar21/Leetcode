# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small, big = p.val, q.val
        if small > big:
            small, big = big, small
        return self.LCA(root, small, big)
    
    def LCA(self, root, small, big):
        if big < root.val:
            return self.LCA(root.left, small, big)
        
        if small > root.val:
            return self.LCA(root.right, small, big)
        
        assert big >= root.val >= small
        return root