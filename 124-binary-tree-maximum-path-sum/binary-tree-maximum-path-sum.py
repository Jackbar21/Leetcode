# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # We must guarantee the path is non-empty.
        max_val = float("-inf")
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val > max_val:
                max_val = node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        # If largest value is negative (or zero), then simply picking 
        # that node will produce the "maximum path sum"
        if max_val <= 0:
            return max_val
        
        # Since there is at least one positive node in the tree, we can
        # use our dp-helper function, which returns 0 on root = None
        self.maxDirectPathSumMemo = {}
        return self.maxPathSumDp(root)

    @cache
    def maxPathSumDp(self, root: Optional[TreeNode]) -> int:
        # Base Case
        if not root:
            return 0

        # Case 1: Largest path goes through root
        case1 = self.maxPathSumThroughRoot(root)

        # Case 2: Largest path belongs in left subtree
        case2 = self.maxPathSumDp(root.left)

        # Case 3: Largest path belongs in right subtree
        case3 = self.maxPathSumDp(root.right)

        return max(case1, case2, case3)
    
    @cache
    def maxPathSumThroughRoot(self, root: Optional[TreeNode]) -> int:
        # Return maximum path sum, such that the path MUST go through 'root'
        res = root.val
        left = self.maxDirectPathSum(root.left)
        right = self.maxDirectPathSum(root.right)

        # Don't have to pick nodes on left/right if produces negative values!
        if left < 0:
            left = 0
        if right < 0:
            right = 0

        return left + root.val + right
    
    def maxDirectPathSum(self, root: Optional[TreeNode]) -> int:
        # Return maximum path sum from root downwards
        if root in self.maxDirectPathSumMemo:
            return self.maxDirectPathSumMemo[root]

        res = 0 if not root else root.val + max(0, self.maxDirectPathSum(root.left), self.maxDirectPathSum(root.right))
        self.maxDirectPathSumMemo[root] = res
        return res
        