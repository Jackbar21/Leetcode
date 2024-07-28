class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # Initialize Neighbors
        neighbors = {
            i: set() for i in range(1,n+1)
        }
        for edge in edges:
            u,v = edge
            neighbors[u].add(v)
            neighbors[v].add(u)

        FIRST, SECOND = 0, 1
        reach_times = {
            i: [float("inf"), float("inf")] for i in range(1,n+1)
        }

        # Run BFS
        # visited = set()
        # double_visited = set()
        q = collections.deque()
        q.append((1, 0)) # (node, reach_time)
        while len(q) > 0:
            node, reach_time = q.popleft()

            if node == n and reach_times[node][SECOND] != float("inf"):
                return reach_times[node][SECOND]

            for neighbor in neighbors[node]:
                
                # Time it takes to reach this neighbor =
                # (1) time to reach node [reach_time] +
                # (2) delay time before signal is green
                # (3) travel time to reach node [time]

                # For (2) delay, there are two cases:
                # Case 1: we are green, so 0 delay
                # Case 2: we are red, so delay 
                # signal is green if whole number is even, else red
                is_green_signal = (reach_time // change) % 2 == 0
                delay = 0 if is_green_signal else change - (reach_time % change)
                neighbor_reach_time = reach_time + delay + time

                # Case 1: double visited
                if reach_times[neighbor][SECOND] != float("inf"):
                    continue
                
                if neighbor_reach_time < reach_times[neighbor][FIRST]:
                    reach_times[neighbor][FIRST] = neighbor_reach_time
                elif reach_times[neighbor][FIRST] < neighbor_reach_time < reach_times[neighbor][SECOND]:
                    reach_times[neighbor][SECOND] = neighbor_reach_time

                q.append(
                    (neighbor, neighbor_reach_time)
                )

        return -1