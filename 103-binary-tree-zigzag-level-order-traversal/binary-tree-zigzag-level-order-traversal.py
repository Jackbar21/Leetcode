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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.populateTree(root, 0)
        return [self.d[i] for i in range(self.maxDepth+1)]
    def populateTree(self, root, depth):
        if not root:
            return
        
        # inorder
        self.populateTree(root.left, depth+1)
        if depth not in self.d:
            self.d[depth] = collections.deque()
        if depth % 2 == 0:
            self.d[depth].append(root.val)
        else:
            self.d[depth].appendleft(root.val)
        self.maxDepth = max(self.maxDepth, depth)
        self.populateTree(root.right, depth+1)