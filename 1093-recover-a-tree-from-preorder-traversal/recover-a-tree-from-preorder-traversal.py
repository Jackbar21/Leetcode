# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        N = len(traversal)
        DASH = "-"
        d = defaultdict(collections.deque)
        depths = collections.deque()
        cur_depth = 0
        i = 0

        # Step 1: Convert 'traversal' string into dictionary of depths-to-values
        # and order of depths traversed from dashes :)
        while i < N:
            char = traversal[i]
            if char == DASH:
                cur_depth += 1
                i += 1
                continue
            
            chars = []
            while char != DASH:
                chars.append(char)
                i += 1
                if i == N:
                    break
                char = traversal[i]
            num = int("".join(chars))

            d[cur_depth].append(num)
            depths.append(cur_depth)
            cur_depth = 0
        
        print(f"{d=}")
        print(f"{depths=}")
        
        # Step 2: Build the tree!
        #assert depths.popleft() == 0
        root = TreeNode(d[depths.popleft()].pop())
        prev_depth = 0
        stack = [root]
        node_to_depth = {root: 0}
        for depth in depths:
            val = d[depth].popleft()
            node = TreeNode(val)
            node_to_depth[node] = depth

            if depth > prev_depth:
                #assert depth == prev_depth + 1
                prev_node = stack[-1]
                #assert not prev_node.left
                prev_node.left = node
                stack.append(node)
                prev_depth = depth
                continue
            
            #        1
            #      /   \
            #     2      5
            #    /      /
            #   3      6
            #  /      /
            # 4      7
            # stack = [5, 6, 7]
            # prev_depth = 3
            # depth = 3
            # node = 7
            # d = {0: [], 1: [], 2: [], 3: []}
            
            if depth == prev_depth:
                #assert len(stack) >= 2
                stack.pop()
                parent_node = stack[-1]
                #assert prev_prev_node.left and not prev_prev_node.right
                parent_node.right = node
                stack.append(node)
                prev_depth = depth
                continue
            
            #assert depth < prev_depth
            while node_to_depth[stack[-1]] != depth - 1:
                stack.pop()
            parent_node = stack.pop()
            #assert parent_node.left and not parent_node.right
            parent_node.right = node
            prev_depth = depth
            stack.append(node)
        
        return root
