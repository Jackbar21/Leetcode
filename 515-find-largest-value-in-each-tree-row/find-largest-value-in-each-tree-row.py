# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        levels = []
        queue = collections.deque([(root, 0)]) # (node, level)
        while len(queue) > 0:
            node, level = queue.popleft()
            # levels[level] = max(node.val, levels.get(level, float("-inf")))
            if level == len(levels):
                levels.append(node.val)
            else:
                levels[-1] = max(node.val, levels[-1])
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return levels


