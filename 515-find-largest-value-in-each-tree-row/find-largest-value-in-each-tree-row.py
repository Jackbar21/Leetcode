# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = {}
        self.maxDepth = 0
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # idea: create a dictionary of elements at each depth,
        # and instead of constructing a minheap at each level
        # and popping the smallest one from each depth for total
        # complexity of O(nlogn), just keep a simple array and
        # get max naively from each depth level which will be
        # total of O(n). Sometimes, simple is better!
        # EDIT: With inorder traversal, we know the max is the
        # last of the array. Still O(n), but even better!!
        # EDIT 2: Nevermind, this is not a BST lol...
        if not root:
            return []
        self.generateValues(root, 0)
        return [max(self.d[key]) for key in range(self.maxDepth+1)]
    def generateValues(self, root, depth):
        if not root:
            return
        
        # inorder traversal
        self.generateValues(root.left, depth+1)
        self.maxDepth = max(self.maxDepth, depth)
        if depth not in self.d:
            self.d[depth] = []
        self.d[depth].append(root.val)
        self.generateValues(root.right, depth+1)