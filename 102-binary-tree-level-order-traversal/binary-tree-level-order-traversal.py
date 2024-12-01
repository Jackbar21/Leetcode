# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level_to_values = defaultdict(list) # level: [nodes at level]
        max_level = 0

        queue = collections.deque([(root, 0)]) # (node, level)
        while len(queue) > 0:
            node, level = queue.pop()
            level_to_values[level].append(node.val)
            if max_level < level:
                max_level = level
            if node.left:
                queue.appendleft((node.left, level + 1))
            if node.right:
                queue.appendleft((node.right, level + 1))


        return [
            level_to_values[level]
            for level in range(max_level + 1)
        ]
