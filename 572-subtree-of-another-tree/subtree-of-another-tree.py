# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return bool(not subRoot) if not root else (isSameTree := lambda root1, root2: (not root1 and not root2) or (root1 and root2 and root1.val == root2.val and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)))(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    