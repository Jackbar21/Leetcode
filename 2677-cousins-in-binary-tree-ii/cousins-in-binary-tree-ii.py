# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node_to_depth = {}
        self.node_to_parent = {}
        self.depth_sums = {}
        self.node_to_replacement_value = {}

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # All we need for each node, is it's depth and parent.
        # We also need to know level sums.
        self.populateDepthsAndParents(root, 0, None)
        self.generateReplacementValues(root)
        return self.updateTree(root)
    
    def populateDepthsAndParents(self, root, depth, parent):
        if not root:
            return
        
        self.node_to_depth[root] = depth
        self.node_to_parent[root] = parent
        self.depth_sums[depth] = self.depth_sums.get(depth, 0) + root.val

        self.populateDepthsAndParents(root.left, depth + 1, root)
        self.populateDepthsAndParents(root.right, depth + 1, root)
        return

    def generateReplacementValues(self, root):
        # Root node is special case, and value is always 0
        self.node_to_replacement_value[root] = 0

        if root.left:
            self.generateReplacementValuesHelper(root.left)

        if root.right:
            self.generateReplacementValuesHelper(root.right)

        return
    
    def generateReplacementValuesHelper(self, root):
        if not root:
            return
        
        depth = self.node_to_depth[root]
        parent = self.node_to_parent[root]
        
        res = self.depth_sums[depth]
        if parent.left:
            res -= parent.left.val
        if parent.right:
            res -= parent.right.val
        
        self.node_to_replacement_value[root] = res

        self.generateReplacementValuesHelper(root.left)
        self.generateReplacementValuesHelper(root.right)
        return
    
    def updateTree(self, root):
        if not root:
            return None
        
        root.val = self.node_to_replacement_value[root]
        root.left = self.updateTree(root.left)
        root.right = self.updateTree(root.right)
        return root
