class MyHashMap:

    def __init__(self):
        self.d = {}

    def put(self, key: int, value: int) -> None:
        self.d[key] = value

    def get(self, key: int) -> int:
        return self.d.get(key,-1)

    def remove(self, key: int) -> None:
        new_d = {}
        for k in self.d:
            if k != key:
                new_d[k] = self.d[k]
        self.d = new_d



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)