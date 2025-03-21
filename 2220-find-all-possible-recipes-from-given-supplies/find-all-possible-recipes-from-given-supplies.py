class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # This problem is simply topological sort in disguise
        # Step 1: Build a graph of nodes and edges
        #   - Nodes: these are ingredients & recipes
        #   - Edges: For each index i, for each node in ingredients[i], edge node to recipes[i]

        # assert len(recipes) == len(ingredients)
        N = len(recipes)
        adj_list = {}
        indegree = defaultdict(int)
        for i in range(N):
            dependency_node = recipes[i]
            for node in ingredients[i]:
                if node not in adj_list:
                    adj_list[node] = [dependency_node]
                else:
                    adj_list[node].append(dependency_node)
            indegree[dependency_node] += len(ingredients[i])
        
        # for ingredient in supplies:
        #     assert indegree[ingredient] == 0

        queue = collections.deque(supplies)
        can_create = set()
        while len(queue) > 0:
            node = queue.popleft()
            # for neigh in adj_list[node]:
            for neigh in adj_list.get(node, []):
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    can_create.add(neigh)
                    queue.append(neigh)
        
        return [recipe for recipe in recipes if recipe in can_create]


