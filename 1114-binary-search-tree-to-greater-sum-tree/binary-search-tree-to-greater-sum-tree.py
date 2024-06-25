# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = {}
        self.sum = None
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root == None:
            return

        if self.sum == None:
            self.sum = self.getSum(root)
        
        # inorder traversal
        root.left = self.bstToGst(root.left)

        # logic here
        self.sum -= root.val
        root.val += self.sum

        # end inorder
        root.right = self.bstToGst(root.right)

        return root

    
    def getSum(self, root):
        return 0 if not root else root.val + self.getSum(root.left) + self.getSum(root.right)