# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Populate hash-map of level to node-value(s) mappings
        depths = defaultdict(collections.deque)

        # Append for even levels, append-left for odd levels (to reverse!)
        queue = collections.deque([(root, 0)]) # (node, level)
        while len(queue) > 0:
            node, level = queue.popleft()
            if level % 2 == 0:
                depths[level].append(node.val)
            else:
                depths[level].appendleft(node.val)
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        # So now, let's revisit the tree in level order again, but this time replacing values
        # with the ones they're meant to be!
        queue = collections.deque([(root, 0)]) # (node, level)
        while len(queue) > 0:
            node, level = queue.popleft()
            node.val = depths[level].popleft()
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return root
