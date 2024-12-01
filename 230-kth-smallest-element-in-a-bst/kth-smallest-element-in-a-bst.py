# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Recursive Solution
        self.last_node_val = None
        self.visited_count = 0
        self.k = k
        self.kthSmallestRec(root)
        return self.last_node_val
    
    def kthSmallestRec(self, root):
        if not root:
            return
        
        # Inorder Traversal!
        self.kthSmallestRec(root.left)
        if self.visited_count >= self.k:
            return
        self.visited_count += 1
        self.last_node_val = root.val
        # self.sorted_arr.append(root.val)
        # if len(self.sorted_arr) >= self.k:
        #     return
        self.kthSmallestRec(root.right)
        