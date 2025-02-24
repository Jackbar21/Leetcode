class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Idea: First, since Bob starts at some node 'bob' and works his way UP the tree, his
        # path is UNIQUE (there is no ambiguity). We can calculate the time at which bob reaches
        # every node in the tree.
        # Once we have that information, we can do a FULL dfs/bfs of the tree from the root node
        # onwards, to calculate Alice's maximum reward. At each node we will check if it's before,
        # at, or after Bob has reached the node himself, to compute the "cost" or "reward" of that node.
        # Whenever we reach a leaf node, that is a full particular path Alice can have taken, and we update
        # the current best result if the reward for current leaf node is largest than the current best
        # found so far. Whenever we backtrack from a node, we will undo the reward/cost for that node,
        # keeping the total reward/cost for every path to a leaf node consistent with what it should be.

        # Step 1: Get all the nodes that Bob reaches and their "reach times". Since the nodes are labeled
        # 0 to n - 1, they are unique (although if they weren't, we could just create TreeNode objects and
        # use their hash as unique IDs).
        N = len(edges) + 1
        # nodes = [TreeNode(i) for i in range(N)]
        # nodes = [i for i in range(N)]
        nodes = range(N)
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)
        root = 0
        
        # Step 2: Get path from bob to 0
        bob_node = bob
        queue = collections.deque() # (node, path)
        queue.append((bob_node, [bob_node]))
        visited = set([bob_node])

        bob_path = None
        while len(queue) > 0:
            node, path = queue.popleft()
            if node == root:
                bob_path = path
                break
            
            # for neigh in node.neighbors:
            for neigh in adj_list[node]:
                if neigh in visited:
                    continue
                visited.add(neigh)
                queue.append((neigh, path + [neigh]))

        visit_times = defaultdict(lambda: float("inf"))
        for time, node in enumerate(bob_path):
            visit_times[node] = time
        #print(f"{visit_times=}")

        # Step 2: We have the times at which bob visited each node (visit_times dict)!
        # Now, let's run a search from root node onwards for Alice, and everytime we reach
        # a leaf node, update cur best result!
        res = float("-inf")
        stack = [(root, 0, 0)] # (node, time, reward)
        visited = set([root])
        while len(stack) > 0:
            node, alice_time, reward = stack.pop()
            bob_time = visit_times[node]
            if alice_time < bob_time:
                reward += amount[node]
            elif alice_time == bob_time:
                reward += amount[node] / 2
            # else, no reward nor cost since gate already open!

            # If node is a leaf node, update cur best result!
            # unvisited_neighbors = [neigh for neigh in node.neighbors if neigh not in visited]
            unvisited_neighbors = adj_list[node] - visited
            if len(unvisited_neighbors) == 0:
                if res < reward:
                    res = reward
                continue
            
            for neigh in unvisited_neighbors:
                stack.append((neigh, alice_time + 1, reward))
                visited.add(neigh)
        
        return int(res)
                


        


        