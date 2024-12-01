# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return 1 + self.goodNodesRec(root.left, root.val) + self.goodNodesRec(root.right, root.val)
        
    def goodNodesRec(self, root, largest):
        if not root:
            return 0
        
        res = int(root.val >= largest)
        if largest < root.val:
            largest = root.val
        
        # Recursive calls...
        res += self.goodNodesRec(root.left, largest)
        res += self.goodNodesRec(root.right, largest)

        return res
