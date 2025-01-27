class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        N = len(favorite)

        # Reversed edges so we can chain connected-components with length 2 cycles!
        adj_list = [[] for _ in range(N)]
        for i in range(N):
            adj_list[favorite[i]].append(i)
        
        res = 0
        length_2_cycle_chain = 0

        unvisited = set(range(N))
        while len(unvisited) > 0:
            node = unvisited.pop()
            node_to_dist = {node: 0}
            cur_dist = 1
            already_seen_cycle = False

            node = favorite[node]
            while node not in node_to_dist:
                if node not in unvisited:
                    already_seen_cycle = True
                    break
                unvisited.remove(node)
                node_to_dist[node] = cur_dist
                node = favorite[node]
                cur_dist += 1
            
            # Already seen & computed cycle, so no need to worry about it again!
            # If it's a closed cycle we've already compared that cycle's length,
            # and if it's a length 2 cycle, we've already added it onto our chain :)
            if already_seen_cycle:
                continue

            # assert node in node_to_dist
            cycle_length = cur_dist - node_to_dist[node]
            if cycle_length > 2:
                # Forms a closed cycle, which CANNOT BE CHAINED!!!
                # Hence, update res to max between res and length of this CLOSED cycle!
                if res < cycle_length:
                    res = cycle_length
                continue
            
            # assert cycle_length == 2
            # Now, we will want to perform a BFS for longest path between each end of this length
            # 2 cycle (not allowing to go through the other node in the length 2 cycle), and remember
            # this result as it can be chained with OTHER components with length 2 cycles!!!

            # Step 1: we need the two nodes in the cycle, and mark them visited so as to NOT permit
            # each one to go through the other!
            # We know 'node' is part of the cycle, so the length 2 cycle must be node and favorite[node]!
            cycle_nodes = [node, favorite[node]]
            
            length_2_cycle_component = 2 # initially 2 for the two cycle nodes themselves!
            for cycle_node in cycle_nodes:
                longest_branch = 0
                # Want to find longest chain from this node, adding cycle nodes as visited first!
                visited = set(cycle_nodes)
                queue = collections.deque([(0, cycle_node)]) # (cost, node)
                while len(queue) > 0:
                    branch_length, node = queue.popleft()
                    unvisited.discard(node)
                    if longest_branch < branch_length:
                        longest_branch = branch_length
                    
                    # This is when we want to consult the reversed-edges 'adj_list' we built earlier,
                    # to find longest chains from cycle nodes from in-to-out favorite-wise!
                    for neigh in adj_list[node]:
                        if neigh in visited:
                            continue
                        
                        queue.append((branch_length + 1, neigh))
                        visited.add(neigh)
                
                length_2_cycle_component += longest_branch

            # Now, chain this length 2 cycle component onto the chain of length-2-cycle components!
            # length_2_cycle_chain.append(length_2_cycle_component)
            length_2_cycle_chain += length_2_cycle_component

        if res < length_2_cycle_chain:
            res = length_2_cycle_chain
        return res
