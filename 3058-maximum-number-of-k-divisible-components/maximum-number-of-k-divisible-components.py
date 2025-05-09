class TreeNode:
    def __init__(self, label, val):
        self.label = label
        self.val = val
        self.children = []
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
        
        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[tree[a]].append(tree[b])
            adj_list[tree[b]].append(tree[a])
        
        # Now, populate the tree!
        queue = collections.deque()
        queue.append((root, None)) # (node, parent)
        visited = set()
        visited.add(root)
        while len(queue) > 0:
            node, parent = queue.popleft()
            node.parent = parent

            children = adj_list[node]
            for child in children:
                if child not in visited:
                    queue.append((child, node))
                    node.children.append(child)
                    visited.add(child)
            continue

        self.res = 0
        self.postorder(root)
        return self.res
    
    def postorder(self, root):
        if not root:
            return
        
        for child in root.children:
            self.postorder(child)

        if (root.val % self.k) == 0:
            self.res += 1
            return

        # Transfer val to parent, since can't cut at node yet!
        root.parent.val += root.val
