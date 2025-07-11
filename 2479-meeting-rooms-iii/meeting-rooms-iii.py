class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = defaultdict(int) # room_number: count used
        d = defaultdict(int)     # room_number: time_available

        for start, end in meetings:
            room = None
            for room_number in range(n):
                if d[room_number] <= start:
                    room = room_number
                    break
            if room is None:
                earliest_available = min(d.values())
                for room_number in range(n):
                    if d[room_number] == earliest_available:
                        room = room_number
                        break
                #print(f"{start=}, {end=}, {earliest_available=}, {room=}")
                meeting_duration = end - start
                d[room] = earliest_available + meeting_duration
            else:
                d[room] = end
            assert room is not None
            #print(f"using room #{room}")
            count[room] += 1
            
            #print(f"{count=}, {d=}, \n")
        
        #print(f"{d=}")
        #print(f"{count=}")

        res = None
        max_count = max(count.values())
        #print(f"{max_count=}")
        for room_number in range(n):
            if count[room_number] == max_count:
                res = room_number
                break
        assert res is not None
        return res 
