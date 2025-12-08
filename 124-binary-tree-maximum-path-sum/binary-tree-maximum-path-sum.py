class Solution:
    def maxPathSum(self, root):
        self.res = float("-inf")
        self.dp(root)
        return self.res

    def dp(self, root):
        if not root:
            return 0
        
        left = self.dp(root.left)
        if left < 0:
            left = 0

        right = self.dp(root.right)
        if right < 0:
            right = 0
        
        # Best path THROUGH this root
        val = left + root.val + right
        if self.res < val:
            self.res = val
        
        # Best single-branch path DOWNWARD
        return root.val + (left if left > right else right)
