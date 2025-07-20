class RandomizedSet:
    def __init__(self):
        self.d = {} # num to index
        self.arr = []

    def insert(self, val: int) -> bool:
        res = val not in self.d
        if res:
            self.arr.append(val)
            self.d[val] = len(self.arr) - 1
        return res

    def remove(self, val: int) -> bool:
        res = val in self.d
        if res:
            last_num = self.arr[-1]
            last_index = self.d[last_num]
            val_index = self.d[val]

            # Swap cur and last
            self.arr[val_index] = last_num
            self.arr[last_index] = val
            self.d[last_num] = val_index
            self.d[val] = last_index

            # Delete val, which is now last element
            assert self.arr.pop() == val
            del self.d[val]

        return res

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.arr) - 1)
        return self.arr[random_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()