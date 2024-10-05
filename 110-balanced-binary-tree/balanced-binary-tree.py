# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = True
        self.heights = {} # TreeNode to height
    def getHeight(self, node):
        if node in self.heights:
            return self.heights[node]
        
        if not node:
            return 0
        
        return 1 + max(
            self.getHeight(node.left),
            self.getHeight(node.right)
        )

    def getHeightAndUpdateRes(self, root):
        if not root:
            return 0
        
        left_height = self.getHeightAndUpdateRes(root.left)
        right_height = self.getHeightAndUpdateRes(root.right)
        diff = abs(left_height - right_height)
        if diff > 1:
            self.res = False

        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.getHeightAndUpdateRes(root)
        return self.res

    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True

    #     left_height = self.getHeight(root.left)
    #     right_height = self.getHeight(root.right)
    #     diff = abs(left_height - right_height)
    #     if diff > 1:
    #         return False

    #     return self.isBalanced(root.left) and self.isBalanced(root.right)
