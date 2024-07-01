# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = {}
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        self.populateTree(root, 0)
        for level in self.d:
            if level % 2 == 0:
                prev_val = float("-inf")
                for val in self.d[level]:
                    if val % 2 == 0 or prev_val >= val:
                        return False
                    prev_val = val
            else:
                prev_val = float("inf")
                for val in self.d[level]:
                    if val % 2 == 1 or prev_val <= val:
                        return False
                    prev_val = val
        
        return True
    
    def populateTree(self, root, depth):
        if not root:
            return
        
        # inorder traversal
        self.populateTree(root.left, depth+1)
        if depth not in self.d:
            self.d[depth] = []
        self.d[depth].append(root.val)
        self.populateTree(root.right, depth+1)
