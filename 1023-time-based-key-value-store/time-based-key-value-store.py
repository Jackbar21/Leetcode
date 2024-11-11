class TimeMap:
    def __init__(self):
        self.d = {} # key to array mappings

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []

        self.d[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d.get(key, [])
        best_val, best_timestamp = "", float("-inf")

        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            cur_val, cur_timestamp = arr[mid]
            if cur_timestamp <= timestamp:
                # Valid case, update current best result if need be
                if cur_timestamp > best_timestamp:
                    best_timestamp = cur_timestamp
                    best_val = cur_val
                
                l = mid + 1
            else:
                r = mid - 1

        return best_val


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)