# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # There are only three possible cases:
        # Case 1: Best solution is in left subtree
        # Case 2: Best solution is in right subtree
        # Case 3: Solution goes through the root. Greedily find the best path including root.
        if not root:
            return 0
        
        case1 = self.maxPathSum(root.left) if root.left else float("-inf")
        case2 = self.maxPathSum(root.right) if root.right else float("-inf")
        case3 = root.val + max(self.greedyPathSum(root.left), 0) + max(self.greedyPathSum(root.right), 0)

        # print(f"{root.val, case1, case2, case3=}")
        return max(case1, case2, case3)
    
    @cache
    def greedyPathSum(self, root):
        if not root:
            return float("-inf")
        
        left_sum = self.greedyPathSum(root.left)
        right_sum = self.greedyPathSum(root.right)


        # case0 = 0 # No nodes
        case1 = root.val # Just root
        # case2 = left_sum # Just left subtree
        # case3 = right_sum # Just right subtree
        case4 = root.val + left_sum # Just root + left subtree
        case5 = root.val + right_sum # Just root + right subtree
        # case6 = root.val + left_sum + right_sum # Root + left subtree + right subtree
        return max(case1, case4, case5)
        