class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # From deltas, pick the starting index where you can obtain a "largest subarray sum" from that
        # index, for the remaining deltas (IGNORING the start ones!) Whenever a negative subarray sum
        # is reached, a simple reset and index-switch will do!
        N = len(gas)
        index = 0
        cur_sum = 0
        delta_sum = 0
        # deltas = [gas[i] - cost[i] for i in range(N)]
        # print(f"{sum(deltas)=}")
        # print(f"{deltas}")
        for i in range(N):
            delta = gas[i] - cost[i]
            delta_sum += delta
            cur_sum += delta
            if cur_sum < 0:
                cur_sum = 0
                index = (i + 1) % N
        
        return index if delta_sum >= 0 else -1
