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
        return self.buildTreeHelper(0, inorder)
    
    def buildTreeHelper(self, preorder_index, inorder):
        if len(self.preorder) == 0:
            return None
        
        if len(inorder) == 0:
            return None

        # preorder_val = self.preorder[preorder_index]
        preorder_val = self.preorder.popleft()
        node = TreeNode(preorder_val)
        # print(f"{preorder_val=}")
        # print(f"{inorder=}")
        
        # assert preorder_val in self.inorder
        index = inorder.index(preorder_val)
        # print(f"{inorder[:index]=}")
        # print(f"{inorder[index+1:]=}")
        # print("")
        # assert inorder_start <= index <= inorder_end
        # assert index != float("inf")

        
        node.left = self.buildTreeHelper(preorder_index + 1, inorder[:index])
        node.right = self.buildTreeHelper(preorder_index + 2, inorder[index+1:])
        return node
