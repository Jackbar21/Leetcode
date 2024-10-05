# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # return self.maxDepthHelper(root, 0)
        if not root:
            return 0

        max_depth = 0
        stack = [(root, 1)]
        while stack:
            root, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if root.left:
                stack.append((root.left, depth + 1))
            if root.right:
                stack.append((root.right, depth + 1))
        
        return max_depth
    
    def maxDepthHelper(self, root, depth):
        if not root:
            return depth
        
        left = self.maxDepthHelper(root.left, depth + 1)
        right = self.maxDepthHelper(root.right, depth + 1)
        return max(left, right)
