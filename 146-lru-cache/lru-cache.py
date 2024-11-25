class ListNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        # Double linked list w/ dummy head & tail
        self.head = ListNode(-1, -1) # dummy
        self.tail = ListNode(-1, -1) # dummy
        self.head.next = self.tail
        self.tail.prev = self.head

        self.d = {} # maps keys to linked list nodes!
        self.capacity = capacity # Maximum length
        

    def get(self, key: int) -> int:
        node = self.d.get(key, None)
        if not node:
            return -1

        res = node.val
        self.update(key) # key is now most-recently-used!
        return res
        

    def put(self, key: int, value: int) -> None:
        d = self.d
        if key in d:
            node = self.d[key]
            node.val = value
            self.update(key)
            return

        # Add node to tail & add to dict/increment length!
        node = ListNode(key, value)
        tail = self.tail
        last_node = tail.prev
        last_node.next = node
        node.next = tail
        tail.prev = node
        node.prev = last_node
        d[key] = node # Add node to dict!

        # Pop node from head if exceeds capacity
        if len(d) > self.capacity:
            first_node = self.head.next
            del d[first_node.key]
            prev_node, next_node = first_node.prev, first_node.next
            prev_node.next = next_node
            next_node.prev = prev_node


    def update(self, key):
        # Update key to become most recently used inside linked list!
        node = self.d[key]
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        # Now add it to end of linked list, i.e. as most-recently-used (MRU!)
        tail = self.tail
        last_node = tail.prev
        last_node.next = node
        node.next = tail
        tail.prev = node
        node.prev = last_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)