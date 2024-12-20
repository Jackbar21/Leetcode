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
            node, level_id = queue.popleft()
            d[level_id].append(node)
            level_id += 1

            left_node = node.left
            if left_node:
                if left_node.left:
                    queue.append((left_node.left, level_id))
                if left_node.right:
                    queue.append((left_node.right, level_id))
            
            right_node = node.right
            if right_node:
                if right_node.left:
                    queue.append((right_node.left, level_id))
                if right_node.right:
                    queue.append((right_node.right, level_id))
        
        for nodes in d.values():
            while len(nodes) > 0:
                left, right = nodes.popleft(), nodes.pop()
                left.val, right.val = right.val, left.val # Python supports swapping like this :)

        return root
        