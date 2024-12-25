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
            if level == len(levels):
                levels.append(node.val)
            elif node.val > levels[level]:
                levels[level] = node.val

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return levels
