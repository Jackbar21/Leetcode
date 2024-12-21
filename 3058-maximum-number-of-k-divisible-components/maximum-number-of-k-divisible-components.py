class TreeNode:
    def __init__(self, label, val):
        self.label = label
        self.val = val
        self.children = set()
        self.parent = None
    
    def __str__(self):
        return f"({self.label=},{self.val=})"

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        self.n = n
        self.k = k
        # First, find the node that has smallest indegree, as that will be our root node!
        indegrees = [0] * n
        for a, b in edges:
            indegrees[a] += 1
            indegrees[b] += 1
        min_val = float("inf")
        root_label = -1
        for i, indegree in enumerate(indegrees):
            if indegree < min_val:
                min_val = indegree
                root_label = i
        assert root_label != None

        # Dictionary -- label (i.e. 0 to n - 1): TreeNode
        tree = {i: TreeNode(i, values[i]) for i in range(n)}
        root = tree[root_label]
        
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[tree[a]].add(tree[b])
            adj_list[tree[b]].add(tree[a])
        
        # Now, populate the tree!
        queue = collections.deque()
        queue.append((root, None)) # (node, parent)
        visited = set()
        # visited.add(root)
        while len(queue) > 0:
            node, parent = queue.popleft()
            node.parent = parent
            if node in visited:
                continue
            visited.add(node)

            children = adj_list[node] - visited
            for child in children:
                queue.append((child, node))
                node.children.add(child)
            continue

        # Level-order tree traversal
        # depths = defaultdict(list)
        # queue = collections.deque([(root, 0)]) # (node, depth)
        # while len(queue) > 0:
        #     node, depth = queue.popleft()
        #     depths[depth].append(node.label)
        #     for child in node.children:
        #         queue.append((child, depth + 1))
        # print(f"{depths=}")
        # for depth in depths:
        #     print(f"level {depth}: {depths[depth]}")

            #       6
            #   1      5

        
        # Let's try an inorder traversal!

        self.res = 0
        self.cur_sum = 0
        self.postorder(root)
        return self.res

        # print(f"{indegrees=}")
        assert root != -1
        return root_label
    
    def postorder(self, root):
        if not root:
            return
        
        # self.inorder(root.left)
        for child in root.children:
            self.postorder(child)
        if (root.val % self.k) == 0:
            self.res += 1
        else:
            parent = root.parent
            assert parent is not None
            parent.val += root.val
        return
        # print(f"{self.cur_sum=}, {root.val=}, {root.label=}")
        # if root.val % self.k == 0:
        #     self.res += (root.val > 0 or self.k == 1)
        # else:
        #     self.cur_sum += root.val
        #     if self.cur_sum % self.k == 0:
        #         self.res += (root.val > 0 or self.k == 1)
        # if root.val % self.k == 0:
        #     self.res += 1
        # else:
        #     parent = root.parent
        #     if parent:
        #         parent.val += root.val
        # self.inorder(root.right)
        # return
    
    @cache
    def sumTree(self, root) -> int:
        if not root:
            return 0
        return root.val + self.sumTree(root.left) + self.sumTree(root.right)

    # @cache
    # def dp(self, root):
    #     # Case 1: Delete no edges
