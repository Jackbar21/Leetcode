class ListNode:
    def __init__(self, key = 0, val = 0, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        # Double linked list w/ dummy head & tail
        self.head = ListNode(-1, -1) # dummy
        self.tail = ListNode(-1, -1) # dummy
        self.head.next = self.tail
        self.tail.prev = self.head

        self.d = {} # maps keys to linked list nodes!
        self.length = 0 # Length of linked list
        self.capacity = capacity # Maximum length
        

    def get(self, key: int) -> int:
        # print(key, self.d)
        # assert key in self.d
        if key not in self.d:
            return -1
        assert len(self.d) == self.length <= self.capacity
        node = self.d[key]
        res = node.val
        self.update(key) # update to MRU
        return res
        

    def put(self, key: int, value: int) -> None:
        assert len(self.d) == self.length <= self.capacity
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.update(key)
            return

        # Add node to tail & add to dict/increment length!
        node = ListNode(key, value)
        last_node = self.tail.prev
        last_node.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = last_node
        self.d[key] = node # Add node to dict!
        self.length += 1

        # Pop node from head if exceeds capacity
        assert len(self.d) == self.length
        if self.length > self.capacity:
            assert self.length - 1 == self.capacity
            first_node = self.head.next
            first_node_key = first_node.key
            prev_node, next_node = first_node.prev, first_node.next
            prev_node.next = next_node
            next_node.prev = prev_node
            assert first_node_key in self.d
            del self.d[first_node_key]
            self.length -= 1
        
        # self.update(key)
    
    def update(self, key):
        # Update key to become most recently used inside linked list!
        assert key in self.d
        assert len(self.d) == self.length <= self.capacity
        node = self.d[key]
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        # Now add it to end of linked list, i.e. as most-recently-used (MRU!)
        last_node = self.tail.prev
        last_node.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = last_node
        return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)