class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        N, M = len(nums), len(edges)

        # We leverage the fact that since this is a TREE, that means EVERY two nodes
        # are connected, which means we can apply on operation on ANY pair of two nodes
        # (u, v) in the graph, NOT just the ones in edges!
        # getDelta = lambda num: (num ^ k) - num
        max_heap = [-((num ^ k) - num) for num in nums] # (delta, num)
        heapq.heapify(max_heap)

        res = sum(nums)
        while len(max_heap) >= 2:
            delta1 = -heapq.heappop(max_heap)
            delta2 = -heapq.heappop(max_heap)
            delta = delta1 + delta2

            if delta <= 0:
                break
            res += delta
        
        return res



    # My attempt at solving this problem before checking out Hints & Discussions!
    def maximumValueSumAttempt(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        N, M = len(nums), len(edges)
        adj_list = {i: set() for i in range(N)}

        def getEdgeCost(u, v):
            res = 0

            old_u, old_v = nums[u], nums[v]
            new_u, new_v = nums[u] ^ k, nums[v] ^ k

            res += (new_u - old_u)
            res += (new_v - old_v)
            return res
        
        for u, v in edges:
            edge_cost = getEdgeCost(u, v)
            adj_list[u].add((v, edge_cost))
            adj_list[v].add((u, edge_cost))
        
        # Want to find path with MAXIMAL sum in Graph!
        # return sum(nums) + sum(max(0, getEdgeCost(u, v)) for u, v in edges)
        res = sum(nums)

        max_heap = [(-getEdgeCost(u, v), u, v, False)] # (edge_cost, u, v, reseen)
        heapq.heapify(max_heap) # O(n)

        while max_heap:
            edge_cost, u, v, reseen = heapq.heappop(max_heap)
            edge_cost = -edge_cost

            if edge_cost != getEdgeCost(u, v):
                heapq.heappush(max_heap, (-getEdgeCost(u, v), u, v, reseen))
                continue
            
            if edge_cost <= 0:
                found_larger = False
                for i, (cost, x, y, seen) in max_heap:
                    cost = getEdgeCost(x, y)
                    max_heap[i] = (-cost, x, y, seen)
                    if cost > 0:
                        found_larger = True
                        break
                if not found_larger:
                    break
                else:
                    continue

                # if reseen:
                #     break
                
                # break # Nothing good for us anymore!
                heapq.heappush(max_heap, (-getEdgeCost(u, v), u, v, True))
            
            res += edge_cost
        
        return res



        ### BATCKTRACK SOLUTION (TLE) ###
        """
        N, M = len(nums), len(edges)
        res = float("-inf")
        cur_sum = sum(nums)
        def backtrack(i):
            nonlocal res
            nonlocal cur_sum
            if i >= M:
                # res = max(res, sum(nums))
                res = max(res, cur_sum)
                return
            
            # Case 1: Don't apply edge
            backtrack(i + 1)

            # Case 2: Apply edge
            u, v = edges[i]
            old_u, old_v = nums[u], nums[v]
            nums[u] ^= k
            nums[v] ^= k
            cur_sum += (nums[u] - old_u)
            cur_sum += (nums[v] - old_v)
            backtrack(i + 1)
            # nums[u] ^= k
            # nums[v] ^= k
            cur_sum -= (nums[u] - old_u)
            cur_sum -= (nums[v] - old_v)
            nums[u] = old_u
            nums[v] = old_v

        backtrack(0)
        return res
        """