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
                left.val, right.val = right.val, left.val # Python supports swapping like this :)
                # tmp = right.val
                # right.val = left.val
                # left.val = tmp
        return root
        
        # Now that we have the value of all the nodes at every odd level,
        # we can reassign their values as desired :)
        queue = collections.deque() # (node, level)
        # TODO: Can I do queue.clear() instead?
        if root.left:
            queue.append((root.left, 1))
            # odd_values.appendleft(root.left.val)
        if root.right:
            queue.append((root.right, 1))
            # odd_values.appendleft(root.right.val)
        
        while len(queue) > 0:
            # assert len(queue) == len(odd_values)
            node, level = queue.popleft()
            # depths[level].append(node.val)
            node.val = d[level].pop()
            # node.val = odd_values.popleft()

            if node.left:
                if node.left.left:
                    queue.append((node.left.left, level + 2))
                    # odd_values.appendleft(node.left.left.val)
                if node.left.right:
                    queue.append((node.left.right, level + 2))
                    # odd_values.appendleft(node.left.right.val)
            
            if node.right:
                if node.right.left:
                    queue.append((node.right.left, level + 2))
                    # odd_values.appendleft(node.right.left.val)
                if node.right.right:
                    queue.append((node.right.right, level + 2))
                    # odd_values.appendleft(node.right.right.val)
        
        return root
    
        

        

        # Append for even d, append-left for odd d (to reverse!)
        # queue = collections.deque([(root, 0)]) # (node, level)
        # while len(queue) > 0:
        #     node, level = queue.popleft()
        #     if level % 2:
        #         d[level].append(node.val)
            
        #     if node.left:
        #         queue.append((node.left, level + 1))
        #     if node.right:
        #         queue.append((node.right, level + 1))
        
        # # So now, let's revisit the tree in level order again, but this time replacing values
        # # with the ones they're meant to be!
        # queue = collections.deque([(root, 0)]) # (node, level)
        # while len(queue) > 0:
        #     node, level = queue.popleft()
        #     if level % 2:
        #         node.val = d[level].pop()
        #     if node.left:
        #         queue.append((node.left, level + 1))
        #     if node.right:
        #         queue.append((node.right, level + 1))
        
        # return root
