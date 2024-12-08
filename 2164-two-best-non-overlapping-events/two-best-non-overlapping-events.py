class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        START, END, VALUE = 0, 1, 2
        events.sort(key = lambda event: event[END])
        prefix_values = []
        max_value = float("-inf")
        for event in events:
            max_value = max(max_value, event[VALUE])
            prefix_values.append(max_value)
        
        res = prefix_values[-1] # Exactly 1 interval case (since can pick AT MOST 2!)
        for event in events:
            max_value = float("-inf")
            start, _, value = event
            l, r = 0, len(events) - 1
            while l <= r:
                mid = (l + r) // 2
                # Want to find largest end time such that it is SMALLER than start,
                # and grab its prefix_values to get max value out of all smaller
                # non-overlapping intervals!
                mid_event = events[mid]
                if mid_event[END] < start:
                    max_value = max(max_value, prefix_values[mid])
                    l = mid + 1
                else:
                    r = mid - 1
            
            res = max(res, value + max_value)

        return res