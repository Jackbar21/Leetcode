class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        self.events, self.memo = sorted(events), {}
        return self.dp(0, k)
    
    def dp(self, i, k):
        if (i, k) in self.memo:
            return self.memo[(i, k)]

        events = self.events
        N = len(events)
        START, END, VALUE = 0, 1, 2

        if k == 0 or i >= N:
            return 0
        
        start, end, value = events[i]

        # Case 1: Skip current event
        case1 = self.dp(i + 1, k)

        # Case 2: Pick current event
        # In this case, we earn value points from event, but can only
        # go to events whose start time is at least end + 1.
        index = i + 1
        while index < N and events[index][START] <= end:
            # Invalid, keep looping!
            index += 1
        case2 = value + self.dp(index, k - 1)

        res = case1 if case1 > case2 else case2
        self.memo[(i, k)] = res
        return res
