class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        print(f"{events=}")
        self.events = events
        self.k = k

        return self.dp(0, k)
    
    @cache
    def dp(self, i, k):
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
        # go to events whose start time is at least end + 1
        i += 1
        while i < N and events[i][START] <= end:
            i += 1
        case2 = value + self.dp(i, k - 1)

        return max(case1, case2)

