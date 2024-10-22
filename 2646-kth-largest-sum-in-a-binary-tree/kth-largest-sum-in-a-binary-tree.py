# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.levels = {} # level: sum
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Step 1: Calculate sum for each level
        self.populateLevelSums(root, 1)

        # Step 2: add each (sum, level) pair to max-heap, and get k'th largest
        sorted_levels = sorted(self.levels.values(), reverse=True)
        return sorted_levels[k - 1] if (k - 1) < len(sorted_levels) else -1
    
    def populateLevelSums(self, root, depth):
        if not root:
            return
        
        self.levels[depth] = self.levels.get(depth, 0) + root.val

        self.populateLevelSums(root.left, depth + 1)
        self.populateLevelSums(root.right, depth + 1)
        return
