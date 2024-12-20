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

        queue = collections.deque() # (node, level_id)
        left_node, right_node = root.left, root.right
        if left_node:
            queue.append((left_node, 0))
        if right_node:
            queue.append((right_node, 0))
        
        while len(queue) > 0:
            node, level = queue.popleft()
            d[level].append(node)

            left_node = node.left
            if left_node:
                if left_node.left:
                    queue.append((left_node.left, level + 1))
                if left_node.right:
                    queue.append((left_node.right, level + 1))
            
            right_node = node.right
            if right_node:
                if right_node.left:
                    queue.append((right_node.left, level + 1))
                if right_node.right:
                    queue.append((right_node.right, level + 1))
        
        for nodes in d.values():
            while len(nodes) > 0:
                left, right = nodes.popleft(), nodes.pop()
                # left.val, right.val = right.val, left.val # Python supports swapping like this :)
                tmp = right.val
                right.val = left.val
                left.val = tmp
        return root
        