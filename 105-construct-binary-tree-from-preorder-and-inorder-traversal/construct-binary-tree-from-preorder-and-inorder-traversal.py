# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = collections.deque(preorder)
        self.inorder = inorder
        return self.buildTreeHelper(0, len(inorder) - 1)
    
    def buildTreeHelper(self, l, r):
        # If either self.preorder or inorder is empty, then return None
        if not self.preorder or l > r:
            return None

        preorder_val = self.preorder.popleft()
        node = TreeNode(preorder_val)
        
        # Find index of 'preorder_val' inside inorder from index 'l' to 'r' inclusive...
        index = -1
        for i in range(l, r + 1):
            if self.inorder[i] == preorder_val:
                index = i
                break
        # assert index != -1
        
        node.left = self.buildTreeHelper(l, index - 1)
        node.right = self.buildTreeHelper(index + 1, r)
        return node
