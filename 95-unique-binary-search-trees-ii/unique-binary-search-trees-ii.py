# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # Since it's BSTs, this makes ordering nice: only smaller numbers on left, and larger numbers on right
        # So we can use dp, where we know smaller numbers MUST go to the left and larger numbers MUST go to the right
        return self.dp(1, n)
    
    # Return all possible BSTs with values in range [i..j]
    def dp(self, i, j):
        # Any number in range [1..n] can be root node
        if i >= j:
            yield TreeNode(i) if i == j else None
            return

        for root in range(i, j + 1):
            left = list(self.dp(i, root - 1))
            right = list(self.dp(root + 1, j))
            for l in left:
                for r in right:
                    node = TreeNode(root)
                    node.left = l
                    node.right = r
                    yield node        
