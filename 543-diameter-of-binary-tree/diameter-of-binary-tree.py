# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node_to_max_depth = { None: 0 }
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Populate each node in tree with it's maximum depth.
        self.populateMaxDepth(root)
        
        # Solve actual problem, now given O(1)
        # lookup time for max-depth for each node
        if not root:
            return 0
        
        # Case 1: Largest diameter passes through the root
        left_max_depth = self.node_to_max_depth[root.left]
        right_max_depth = self.node_to_max_depth[root.right]
        case1 = left_max_depth + right_max_depth

        # Case 2: Largest diameter in left subtree
        case2 = self.diameterOfBinaryTree(root.left)

        # Case 3: Largest diameter in right subtree
        case3 = self.diameterOfBinaryTree(root.right)

        # Return largest diameter from all three cases
        return max(case1, case2, case3)

    def populateMaxDepth(self, root):
        # Already computed root's max depth, so return
        if root in self.node_to_max_depth:
            return
        
        # Populate left and right subtree's max depths as needed
        self.populateMaxDepth(root.left)
        self.populateMaxDepth(root.right)
        
        # Update root's max depth, which is 1 more than largest
        # depth between left and right subtrees
        self.node_to_max_depth[root] = 1 + max(
            self.node_to_max_depth[root.left],
            self.node_to_max_depth[root.right]
        )