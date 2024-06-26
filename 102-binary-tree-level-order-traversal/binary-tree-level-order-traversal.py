# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = {}
        self.maxDepth = -1
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.generateArr(root, depth=0)
        res = []
        for i in range(self.maxDepth + 1):
            res.append(self.d[i])
        return res
    
    def generateArr(self, root, depth):
        if not root:
            return
        self.maxDepth = max(self.maxDepth, depth)
        
        self.d[depth] = self.d.get(depth, []) + [root.val]
        self.generateArr(root.left, depth+1)
        self.generateArr(root.right, depth+1)
