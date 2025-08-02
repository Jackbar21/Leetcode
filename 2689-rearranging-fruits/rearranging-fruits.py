class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        d1, d2 = defaultdict(int), defaultdict(int)
        for num in basket1:
            d1[num] += 1
        for num in basket2:
            d2[num] += 1
        unique_fruit_costs = d1.keys() | d2.keys()
        
        move_costs = []
        for cost in unique_fruit_costs:
            freq1 = d1[cost]
            freq2 = d2[cost]
            if (freq1 + freq2) % 2 == 1:
                return -1
            
            if freq1 == freq2:
                continue
            
            small, big = (freq1, freq2) if freq1 < freq2 else (freq2, freq1)
            fruits_to_move = (big - small) // 2
            move_costs.extend([cost] * fruits_to_move)
        
        move_costs.sort()
        res = 0
        
        # For each element in move_costs, we delete smallest & largest at same time.
        # Added cost is always smallest fruit value of two, so focus on first half
        # for res costs.
        # If exchange fruits directly, then take that smallest of two fruit costs,
        # otherwise exchange via smallest cost fruit once and again on way back as
        # "intermediary" fruit. Obviously, only exhange fruits directly if cheaper.
        N = len(move_costs)
        min_move_cost = 2 * min(unique_fruit_costs)
        for i in range(N // 2):
            cost = move_costs[i]
            res += cost if cost < min_move_cost else min_move_cost
        return res
