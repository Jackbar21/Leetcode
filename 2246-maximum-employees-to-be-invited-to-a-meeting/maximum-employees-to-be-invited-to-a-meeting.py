class Solution:
    # SOLUTION FROM EDITORIAL... USING IT TO NOT LOSE MY STREAK!
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_degree = [0] * n

        # Calculate in-degree for each node
        for person in range(n):
            in_degree[favorite[person]] += 1

        # Topological sorting to remove non-cycle nodes
        q = deque()
        for person in range(n):
            if in_degree[person] == 0:
                q.append(person)
        depth = [1] * n  # Depth of each node

        while q:
            current_node = q.popleft()
            next_node = favorite[current_node]
            depth[next_node] = max(depth[next_node], depth[current_node] + 1)
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                q.append(next_node)

        longest_cycle = 0
        two_cycle_invitations = 0

        # Detect cycles
        for person in range(n):
            if in_degree[person] == 0:  # Already processed
                continue

            cycle_length = 0
            current = person
            while in_degree[current] != 0:
                in_degree[current] = 0  # Mark as visited
                cycle_length += 1
                current = favorite[current]

            if cycle_length == 2:
                # For 2-cycles, add the depth of both nodes
                two_cycle_invitations += depth[person] + depth[favorite[person]]
            else:
                longest_cycle = max(longest_cycle, cycle_length)

        return max(longest_cycle, two_cycle_invitations)

    def maximumInvitationsFailedAttempt(self, favorite: List[int]) -> int:
        # For Disjoint Sets, we need a union function, as well as a find function.
        # Initially, all nodes are in their own set
        N = len(favorite)
        # parent = {node: node for node in range(N)}
        adj_list = defaultdict(list)
        for i in range(N):
            adj_list[favorite[i]].append(i)
        # favorite = adj_list
        print(f"{adj_list=}")

        # Idea: In order for a group of employees to sit together, they MUST form a cycle!

        max_len = 0
        max_path = None
        # Idea: run a dfs from each node, and keep track of longest len!
        for i in range(N):
            print(f"{i=}")
            queue = collections.deque([(1, i, [i])]) # (cost, node, path)
            available = defaultdict(lambda: 2)
            # available[i] -= 1
            while len(queue) > 0:
                cost, node, path = queue.popleft()
                if cost > max_len:
                    max_len = cost
                    max_path = path
                
                if node not in favorite:
                    continue
                neighbor = favorite[node]
                if available[node] > 0 and available[neighbor] > 0:
                    available[node] -= 1
                    available[neighbor] -= 1
                    queue.append((cost + 1, neighbor, path + [neighbor]))
                    # visited.add(neighbor)

            print(f"{max_len=}, {max_path=}")
        
        return max_len

        

# 0
#    \
# 1 <-> 2
#    /
# 3