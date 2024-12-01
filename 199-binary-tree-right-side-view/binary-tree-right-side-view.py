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

        level_to_value = {}
        max_level = 0

        queue = collections.deque([(root, 0)]) # (node, level)
        while len(queue) > 0:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

            # Since we add node.left before node.right for each node we pop
            # from the queue, whenever we traverse a node, we can be sure
            # it's the rightmost node we've seen AT ITS LEVEL! Hence, everytime
            # we see such a node (i.e. such as right now!), we will append the
            # value at key=level inside level_to_value dict with node's value :)
            level_to_value[level] = node.val
            # if max_level < level:
            #     max_level = level

        return [
            level_to_value[level]
            for level in level_to_value
        ]