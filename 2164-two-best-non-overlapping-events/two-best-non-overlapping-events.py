class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        START, END, VALUE = 0, 1, 2
        events.sort(key = lambda event: event[END])
        prefix_values = []
        max_value = 0
        for event in events:
            if event[VALUE] > max_value:
                max_value = event[VALUE]
            prefix_values.append(max_value)
        
        res = max_value # Exactly 1 interval case (since can pick AT MOST 2!)
        for event in events:
            max_val = 0
            start, _, value = event
            
            l, r = 0, len(events) - 1
            while l <= r:
                mid = (l + r) // 2
                # Want to find largest end time such that it is SMALLER than start,
                # and grab its prefix_values to get max value out of all smaller
                # non-overlapping intervals!
                if events[mid][END] < start:
                    max_val = prefix_values[mid]
                    l = mid + 1
                else:
                    r = mid - 1
            
            if value + max_val > res:
                res = value + max_val

        return res