# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Populate hash-map of level-to-nodes mappings
        d = defaultdict(collections.deque) # level: [nodes...]

        queue = collections.deque() # (node, level)
        if root.left:
            queue.append((root.left, 1))
        if root.right:
            queue.append((root.right, 1))
        
        while len(queue) > 0:
            node, level = queue.popleft()
            d[level].append(node)

            if node.left:
                if node.left.left:
                    queue.append((node.left.left, level + 2))
                if node.left.right:
                    queue.append((node.left.right, level + 2))
            
            if node.right:
                if node.right.left:
                    queue.append((node.right.left, level + 2))
                if node.right.right:
                    queue.append((node.right.right, level + 2))
        
        for nodes in d.values():
            while len(nodes) > 0:
                left, right = nodes.popleft(), nodes.pop()
                # left.val, right.val = right.val, left.val # Python supports swapping like this :)
                tmp = right.val
                right.val = left.val
                left.val = tmp
        return root
        