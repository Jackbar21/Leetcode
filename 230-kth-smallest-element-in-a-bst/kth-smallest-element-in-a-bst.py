# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.sorted_arr = []
        self.inorder(root)
        # print(f"{self.sorted_arr=}")
        return self.sorted_arr[k - 1]

    def inorder(self, root):
        if not root:
            return
        
        # Inorder Traversal!
        self.inorder(root.left)
        self.sorted_arr.append(root.val)
        self.inorder(root.right)
