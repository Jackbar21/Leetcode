# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.memo = {}
        return self.dp(root, True)
    
    def dp(self, node: Optional[TreeNode], can_rob: bool) -> int:
        if (node, can_rob) in self.memo:
            return self.memo[(node, can_rob)]

        # Base Case:
        if not node:
            return 0

        # Case 1: Rob current node (only if 'can_rob' is True)
        case1 = float("-inf")
        if can_rob:
            case1 = node.val + self.dp(node.left, False) + self.dp(node.right, False)

        # Case 2: Don't rob current node
        case2 = self.dp(node.left, True) + self.dp(node.right, True)

        res = max(case1, case2)
        self.memo[(node, can_rob)] = res
        return res
