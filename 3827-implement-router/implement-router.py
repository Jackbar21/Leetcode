class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = collections.deque()   # holds (src, dst, ts)
        self.packet_set = set()            # detect duplicates
        self.dest_map = collections.defaultdict(list)  # dst -> sorted list of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False

        # Evict if full
        if len(self.queue) == self.memoryLimit:
            old_src, old_dst, old_ts = self.queue.popleft()
            self.packet_set.remove((old_src, old_dst, old_ts))
            # remove old_ts from dest_map[old_dst]
            lst = self.dest_map[old_dst]
            idx = bisect.bisect_left(lst, old_ts)
            lst.pop(idx)

        # Add packet
        self.queue.append(packet)
        self.packet_set.add(packet)
        bisect.insort(self.dest_map[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        src, dst, ts = self.queue.popleft()
        self.packet_set.remove((src, dst, ts))
        lst = self.dest_map[dst]
        idx = bisect.bisect_left(lst, ts)
        lst.pop(idx)
        return [src, dst, ts]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        lst = self.dest_map.get(destination, [])
        if not lst:
            return 0
        left = bisect.bisect_left(lst, startTime)
        right = bisect.bisect_right(lst, endTime)
        return right - left
