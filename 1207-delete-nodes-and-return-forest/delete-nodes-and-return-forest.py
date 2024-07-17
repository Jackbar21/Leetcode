# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = None
        self.found = False
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.res = [root]
        for val in to_delete:
            for i in range(len(self.res)):
                rt = self.res[i]
                self.res[i] = self.delNode(rt, val)

                if self.found:
                    self.found = False
                    break

        return [i for i in self.res if i is not None]
        
    def delNode(self, root, val):
        if not root:
            return root
        
        if root.val != val:
            root.left = self.delNode(root.left, val)
            root.right = self.delNode(root.right, val)
            return root

        # root.val == val
        if root.left:
            self.res.append(root.left)
        if root.right:
            self.res.append(root.right)
        self.found = True
        return None