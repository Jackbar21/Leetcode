class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # This problem is simply topological sort in disguise

        # Step 1: Build a graph of nodes and edges
        #   - Nodes: these are ingredients & recipes
        #   - Edges: For each index i, for each node in ingredients[i], edge node to recipes[i]

        # assert len(recipes) == len(ingredients)
        N = len(recipes)
        adj_list = defaultdict(set)
        for i in range(N):
            dependency_node = recipes[i]
            for node in ingredients[i]:
                adj_list[node].add(dependency_node)
        
        indegree = defaultdict(int)
        for node in adj_list:
            for neigh in adj_list[node]:
                indegree[neigh] += 1
        
        for ingredient in supplies:
            assert indegree[ingredient] == 0

        # print(f"{indegree=}")
        queue = collections.deque(supplies)
        topo_sort = set()
        while len(queue) > 0:
            node = queue.popleft()
            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    topo_sort.add(neigh)
                    queue.append(neigh)
        
        return [
            recipe
            for recipe in recipes
            if recipe in topo_sort
        ]


