# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSumThroughRootMemo = {}
        self.maxDirectPathSumMemo = {}
        self.maxPathSumDpMemo = {}
        res = self.maxPathSumDp(root)
        if res > 0:
            return res
        
        # Since result was zero, it could have been because our dp-helper
        # function returns 0 on null nodes, but it very well could be
        # that every node in the tree is negative. Hence, in this case,
        # the maximum path sum will simply be the value of the largest node
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
        
        return max_val

    def maxPathSumDp(self, root: Optional[TreeNode]) -> int:
        if root in self.maxPathSumDpMemo:
            return self.maxPathSumDpMemo[root]

        # Base Case
        if not root:
            return 0

        # Case 1: Largest path goes through root
        case1 = self.maxPathSumThroughRoot(root)

        # Case 2: Largest path belongs in left subtree
        case2 = self.maxPathSumDp(root.left)

        # Case 3: Largest path belongs in right subtree
        case3 = self.maxPathSumDp(root.right)

        res = case1 if case1 > case2 and case1 > case3 else case2 if case2 > case3 else case3
        self.maxPathSumDpMemo[root] = res
        return res
    
    def maxPathSumThroughRoot(self, root: Optional[TreeNode]) -> int:
        # Return maximum path sum, such that the path MUST go through 'root'
        if root in self.maxPathSumThroughRootMemo:
            return self.maxPathSumThroughRootMemo[root]

        res = root.val
        left = self.maxDirectPathSum(root.left)
        right = self.maxDirectPathSum(root.right)

        # Don't have to pick nodes on left/right if produces negative values!
        if left < 0:
            left = 0
        if right < 0:
            right = 0

        res = left + root.val + right
        self.maxPathSumThroughRootMemo[root] = res
        return res
    
    def maxDirectPathSum(self, root: Optional[TreeNode]) -> int:
        # Return maximum path sum from root downwards
        if root in self.maxDirectPathSumMemo:
            return self.maxDirectPathSumMemo[root]

        res = 0 if not root else root.val + max(0, self.maxDirectPathSum(root.left), self.maxDirectPathSum(root.right))
        self.maxDirectPathSumMemo[root] = res
        return res
        