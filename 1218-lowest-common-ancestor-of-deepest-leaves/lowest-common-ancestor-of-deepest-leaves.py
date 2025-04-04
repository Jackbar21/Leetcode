# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Step 1: Get deepest leaves!
        is_leaf = lambda node: not node.left and not node.right
        node_to_depth = {} # node-to-depth dictionary
        depth_to_nodes = defaultdict(list)
        node_to_parent = {}
        max_depth = 0

        queue = collections.deque([(0, root)]) # (depth, node)
        while queue:
            depth, node = queue.popleft()
            if max_depth < depth:
                max_depth = depth
            node_to_depth[node] = depth
            depth_to_nodes[depth].append(node)

            if (left_child := node.left) is not None:
                node_to_parent[left_child] = node
                queue.append((depth + 1, left_child))

            if (right_child := node.right) is not None:
                node_to_parent[right_child] = node
                queue.append((depth + 1, right_child))

        parents = depth_to_nodes[max_depth]
        assert len(parents) >= 1
        while len(parents) > 1:
            parents = set(node_to_parent[node] for node in parents)
        return parents.pop()

