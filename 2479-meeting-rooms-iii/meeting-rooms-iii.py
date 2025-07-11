class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # assert meetings == sorted(meetings)
        meetings.sort()
        # used = [0] * (n + 1)
        count = {room_number: 0 for room_number in range(n)}

        # (time_available, room_number)
        # min_heap = [(0, room_number) for room_number in range(1, n + 1)]
        # heapq.heapify(min_heap)
        # #print(f"{min_heap=}")
        d = {room_number: 0 for room_number in range(n)} # room_number: time_available

        for start, end in meetings:
            # Grab earliest meeting 
            room = None
            for room_number in range(n):
                if d[room_number] <= start:
                    room = room_number
                    break
            if room is None:
                #print(f"room is None, {d=}")
                assert (earliest_available := min(d.values())) > start
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
