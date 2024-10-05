# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node_to_depth = {}
        self.node_to_max_depth = {None: 0}
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # self.populateDepths(root, 1)
        self.getMaxDepth(root)
        #print(self.node_to_max_depth)
        # return 1
        return self.diameterOfBinaryTreeHelper(root, 0)
    
    # def populateDepths(self, root, depth):
    #     if not root or root in self.node_to_depth:
    #         return
        
    #     # assert root not in node_to_depth
    #     self.node_to_depth[root.val] = depth
    #     self.populateDepths(root.left, depth + 1)
    #     self.populateDepths(root.right, depth + 1)
    #     return

    def getMaxDepth(self, root):
        if root in self.node_to_max_depth:
            return
        
        if root.left not in self.node_to_max_depth:
            self.getMaxDepth(root.left)
        if root.right not in self.node_to_max_depth:
            self.getMaxDepth(root.right)
        
        self.node_to_max_depth[root] = 1 + max(
            self.node_to_max_depth[root.left],
            self.node_to_max_depth[root.right]
        )
        return
        
        #print(root in self.node_to_max_depth, root.val)
        assert root not in self.node_to_max_depth
        self.node_to_max_depth[root] = 1 + max(
            self.getMaxDepth(root.left),
            self.getMaxDepth(root.right)
        )
        return self.node_to_max_depth[root]


    def diameterOfBinaryTreeHelper(self, root, depth):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 0
        
        # Case 1: Go through the root
        # left_depth = self.getMaxDepth(root.left)
        # right_depth = self.getMaxDepth(root.right)
        left_depth = self.node_to_max_depth[root.left]
        right_depth = self.node_to_max_depth[root.right]
        case1 = left_depth + right_depth
        ##print(f"{left_depth=}, {right_depth=}, {case1=}")


        # Case 2: only consider left subtree
        case2 = self.diameterOfBinaryTree(root.left)
        # Case 3: only consider right subtree
        case3 = self.diameterOfBinaryTree(root.right)
        ##print(f"{case2=}")
        ##print(f"{case3=}")
        ##print(f"{max(case1, case2, case3)=}")
        return max(case1, case2, case3)
        
        # if not root.left:
        #     assert root.right
        #     return 1 + self.diameterOfBinaryTree(root.right)
        
        # if not root.right:
        #     assert root.left
        #     return 1 + self.diameterOfBinaryTree(root.left)
        

        
