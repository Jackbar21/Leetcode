# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pairs = set()
        self.leaves = []
    
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if distance < 2:
            return 0

        if not root or self.isLeaf(root):
            return len(self.pairs) // 2
        
        if not root.left:
            return self.countPairs(root.right, distance)
        
        if not root.right:
            return self.countPairs(root.left, distance)
        
        total = 0
        # Case 1: pairs of leaves to the left of root
        total += self.countPairs(root.left, distance)

        # Case 2: pairs of leaves to the right of root
        total += self.countPairs(root.right, distance)

        # Case 3: pairs of leaves where one is to the left of root, 
        #         and other to the right
        self.leaves = []
        self.populateLeaves(root.left, 1)
        left_leaves = self.leaves

        self.leaves = []
        self.populateLeaves(root.right, 1)
        right_leaves = self.leaves

        for left_leaf, lDist in left_leaves:
            for right_leaf, rDist in right_leaves:
                if lDist + rDist <= distance:
                    self.pairs.add((left_leaf, right_leaf))
                    self.pairs.add((right_leaf, left_leaf))

        return len(self.pairs) // 2
    
    def populateLeaves(self, root, distance):
        if not root:
            return
        
        if self.isLeaf(root):
            self.leaves.append((root, distance))
        
        self.populateLeaves(root.left, distance + 1)
        self.populateLeaves(root.right, distance + 1)

    def isLeaf(self, root):
        if not root:
            return False
        
        return not root.left and not root.right