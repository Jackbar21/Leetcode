# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        if not root.left and not root.right:
            if root.val == key:
                return None
            return root
        
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            nxt = root.right
            while nxt.left:
                nxt = nxt.left
            root.val = nxt.val
            root.right = self.deleteNode(root.right, nxt.val)
            return root

            # scrap below...
            if not root.right:
                return root.left
            nxt = root.right
            if not nxt.left:
                root.val = nxt.val
                root.right = nxt.right
            else:
                while nxt.left.left:
                    nxt = nxt.left
                root.val = nxt.left.val
                nxt.left = None
            # while nxt.left:
            #     nxt = nxt.left
            # v = nxt.val
            # nxt = None
            # root.val = v
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root
            