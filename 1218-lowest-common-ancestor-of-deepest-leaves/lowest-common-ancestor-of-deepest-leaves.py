# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: Get deepest leaves!
        node_to_parent = {}
        depth_to_nodes = defaultdict(list)
        max_depth = 0
        queue = collections.deque([(0, root)]) # (depth, node)
        while queue:
            depth, node = queue.popleft()
            if max_depth < depth:
                max_depth = depth
            depth_to_nodes[depth].append(node)

            # Add left child if exists!
            if (left_child := node.left):
                node_to_parent[left_child] = node
                queue.append((depth + 1, left_child))

            # Add right child if exists!
            if (right_child := node.right):
                node_to_parent[right_child] = node
                queue.append((depth + 1, right_child))

        # Get leaf nodes at deepest depth!
        parents = depth_to_nodes[max_depth]
        # Keep getting the current nodes' parents until reach one "common" parent,
        # which will hence be the Lowest Common Ancestor as wanted!
        while len(parents) > 1:
            parents = set(node_to_parent[node] for node in parents)
        # Return Lowest Common Ancestor!
        return parents.pop()
