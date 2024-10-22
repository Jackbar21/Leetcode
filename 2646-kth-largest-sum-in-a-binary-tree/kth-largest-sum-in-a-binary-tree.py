# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.levelSums = {} # level: sum
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Step 1: Calculate sum for each level
        self.populateLevelSums(root, 1) # O(n)

        # Step 2: add each (sum, level) pair to max-heap, and get k'th largest
        # Firstly, if there are less than k levels in total, then there is no solution.
        if len(self.levelSums) < k:
            return -1

        # Otherwise, get k'th largest using a max heap :)
        # This is done in O(klogn) time, instead of O(nlogn) time using sorting!
        # This is because even though number of levels can be n in worst case.
        max_heap = [-levelSum for levelSum in self.levelSums.values()]
        heapq.heapify(max_heap) # O(h), where h is height of the tree (worst case h == n)
        for _ in range(k - 1):
            heapq.heappop(max_heap)
        return -max_heap[0]

        # Instead of heap can use sorting, but time complexity is O(hlogh), 
        # where h is the height of the tree. In worst case, h = n, where n
        # is the number of nodes in the tree, so worst case is actually O(nlogn).
        sorted_levels = sorted(self.levelSums.values(), reverse=True) 
        return sorted_levels[k - 1] if (k - 1) < len(sorted_levels) else -1
    
    def populateLevelSums(self, root, level):
        if not root:
            return
        
        self.levelSums[level] = self.levelSums.get(level, 0) + root.val

        self.populateLevelSums(root.left, level + 1)
        self.populateLevelSums(root.right, level + 1)
        return
