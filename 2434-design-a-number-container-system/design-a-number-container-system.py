class NumberContainers:

    def __init__(self):
        self.index_to_num = {}
        self.num_to_indices = defaultdict(list)
        

    def change(self, index: int, number: int) -> None:
        # if index not in self.index_to_num:
        #     self.index_to_num[index] = number
        #     return
        
        # # Otherwise, need to replace current number!
        self.index_to_num[index] = number
        heapq.heappush(self.num_to_indices[number], index)
        

    def find(self, number: int) -> int:
        min_heap = self.num_to_indices[number]
        while len(min_heap) > 0 and self.index_to_num[min_heap[0]] != number:
            heapq.heappop(min_heap)
        return min_heap[0] if len(min_heap) > 0 else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)