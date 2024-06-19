# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s, b = (p, q) if p.val < q.val else (q, p)
        assert s.val < b.val

        if root == p or root == q:
            return root
    
        # s < root < b
        if s.val < root.val < b.val:
            return root
        
        # s < b < root
        if b.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # root < s < b
        assert root.val < s.val
        return self.lowestCommonAncestor(root.right, p, q)