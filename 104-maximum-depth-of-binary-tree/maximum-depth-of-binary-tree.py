# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthAcc(root, 0)
    def maxDepthAcc(self, root: Optional[TreeNode], depth: int) -> int:
        if root is None:
            return depth
        if root.left is None and root.right is None:
            return depth + 1

        return max(
            self.maxDepthAcc(root.left, depth + 1),
            self.maxDepthAcc(root.right, depth + 1)
        )