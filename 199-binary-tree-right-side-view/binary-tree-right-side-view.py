# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([(0, root)]) # (depth, node)
        depths = []
        max_depth = 0
        while queue:
            depth, node = queue.popleft()
            if len(depths) <= depth:
                depths.append(node.val)
            else:
                depths[depth] = node.val

            if node.left:
                queue.append((depth + 1, node.left))
            
            if node.right:
                queue.append((depth + 1, node.right))
        
        return depths
