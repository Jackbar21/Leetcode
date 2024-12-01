# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.nodes_visited = 0
        self.result = None
        self.inorder(root)
        return self.result

    def inorder(self, root):
        if not root:
            return
        
        # Inorder Traversal!
        self.inorder(root.left)
        self.nodes_visited += 1
        if self.nodes_visited == self.k:
            self.result = root.val
        self.inorder(root.right)
