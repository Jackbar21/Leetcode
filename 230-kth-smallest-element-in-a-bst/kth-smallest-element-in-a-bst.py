# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Recursive Solution
        self.sorted_arr = []
        self.k = k
        self.kthSmallestRec(root)
        return self.sorted_arr[k - 1]
    
    def kthSmallestRec(self, root):
        if not root:
            return
        
        # Inorder Traversal!
        self.kthSmallestRec(root.left)
        self.sorted_arr.append(root.val)
        if len(self.sorted_arr) >= self.k:
            return
        self.kthSmallestRec(root.right)
        