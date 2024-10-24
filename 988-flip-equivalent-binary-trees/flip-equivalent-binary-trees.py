# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # If either root is None, return True if and only if both roots are None
        if not root1 or not root2:
            return not root1 and not root2

        if root1.val != root2.val:
            return False
        
        # IDEA: Never touch root2, only try to make root1 equal to root2. 
        # I.e. pick a tree to modify, and stick to that decision 'til the end.

        # Case 1: Don't swap root1's children
        case1 = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        if case1:
            return True

        # Case 2: Swap root1's children
        root1.left, root1.right = root1.right, root1.left
        case2 = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        if case2:
            return True
        
        # Neither case1 nor case2 was true, so no -- the trees are NOT flip equivalent!
        return False
