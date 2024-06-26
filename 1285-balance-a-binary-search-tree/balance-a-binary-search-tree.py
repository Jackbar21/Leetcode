# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.values = None
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if self.values == None:
            self.values = []
            self.generateValues(root)
        
        return self.balBST(0, len(self.values)-1)
    
    def balBST(self, l, r):
        if l > r:
            return None
        
        mid = l + (r - l)//2
        root = TreeNode(self.values[mid])
        root.left = self.balBST(l, mid-1)
        root.right = self.balBST(mid+1, r)

        return root
    
    def generateValues(self, root):
        if not root:
            return
        # inorder traversal
        self.generateValues(root.left)
        self.values.append(root.val)
        self.generateValues(root.right)