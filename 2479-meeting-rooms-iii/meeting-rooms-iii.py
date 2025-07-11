class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = [0] * n # room_number: count used
        d = [0] * n     # room_number: time_available

        for start, end in meetings:
            room = None
            for room_number in range(n):
                if d[room_number] <= start:
                    room = room_number
                    break
            if room is None:
                earliest_available = float("inf")
                for room_number in range(n):
                    if (room_availability := d[room_number]) < earliest_available:
                        room = room_number
                        earliest_available = room_availability
                meeting_duration = end - start
                d[room] = earliest_available + meeting_duration
            else:
                d[room] = end

            count[room] += 1
        

        res = None
        max_count = float("-inf")
        for room_number in range(n):
            if (room_count := count[room_number]) > max_count:
                res = room_number
                max_count = room_count
        return res 
