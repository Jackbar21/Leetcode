class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        assert len(gas) == len(cost) == N

        deltas = [gas[i] - cost[i] for i in range(N)]
        print(f"{deltas}")

        # From deltas, pick the starting index where you can obtain a "largest subarray sum" from that
        # index, for the remaining deltas (IGNORING the start ones!) Whenever a negative subarray sum
        # is reached, a simple reset and index-switch will do!
        index = 0
        cur_sum = 0
        for i, delta in enumerate(deltas):
            # if cur_sum < 0:
            #     index = i
            cur_sum += delta
            if cur_sum < 0:
                cur_sum = 0
                index = (i + 1) % N
        
        # print(f"{cur_sum=}, {index=}")
        # Now simulate from index!
        i = index
        cur_gas = gas[i]
        for _ in range(N):
            cur_gas -= cost[i]
            if cur_gas < 0:
                return -1

            i = (i + 1) % N
            cur_gas += gas[i]

        return index
        
            



        # Start off with the gas station with cheapest price-to-gas ratio initially
        # best_price_to_gas_ratio = float("inf")
        # best_index = None
        # for i in range(N):
        #     price_to_gas_ratio = cost[i] / gas[i]
        #     if price_to_gas_ratio < best_price_to_gas_ratio:
        #         best_price_to_gas_ratio = price_to_gas_ratio
        #         best_index = i
        min_price = (cost[0], -gas[0])
        min_price_index = 0
        for price_index, price in enumerate(cost):
            # if price < min_price:
            if (price, -gas[price_index]) < min_price:
                min_price = (price, -gas[price_index])
                min_price_index = price_index
        
        # Now, simulate from this index
        i = min_price_index
        cur_gas = gas[i]
        for _ in range(N):
            cur_gas -= cost[i]
            if cur_gas < 0:
                return -1

            i = (i + 1) % N
            cur_gas += gas[i]

        return min_price_index