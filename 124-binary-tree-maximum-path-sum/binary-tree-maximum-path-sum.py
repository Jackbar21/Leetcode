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
            return float("-inf")
        
        case1 = self.maxPathSum(root.left)
        case2 = self.maxPathSum(root.right)

        left_sum = self.greedyPathSum(root.left)
        right_sum = self.greedyPathSum(root.right)
        case3 = root.val
        if left_sum > 0:
            case3 += left_sum
        if right_sum > 0:
            case3 += right_sum

        # return max(case1, case2, case3)
        return case1 if case1 > case2 and case1 > case3 else case2 if case2 > case3 else case3
    
    @cache
    def greedyPathSum(self, root):
        if not root:
            return float("-inf")

        left_sum = self.greedyPathSum(root.left)
        right_sum = self.greedyPathSum(root.right)

        case1 = root.val                # Just root
        case2 = root.val + left_sum     # Just root + left subtree
        case3 = root.val + right_sum    # Just root + right subtree
        # return max(case1, case2, case3)
        return case1 if case1 > case2 and case1 > case3 else case2 if case2 > case3 else case3
        