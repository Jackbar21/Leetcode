class PriorityNode:
    def __init__(self, priority = 0):
        self.priority = priority
        self.next = None
        self.prev = None
        self.keys = set()
    def add(self, key):
        self.keys.add(key)
    def remove(self, key):
        # assert key in self.keys
        self.keys.remove(key)
    def isEmpty(self):
        return len(self.keys) == 0
    def getKey(self):
        # assert not self.isEmpty()
        key = self.keys.pop()
        self.add(key)
        return key
    def __str__(self):
        return f"prio={self.priority}, keys={self.keys}, prev={self.prev.priority if self.prev else None}, next={self.next.priority if self.next else None}"

class AllOne:
    def __init__(self):
        self.keyToNode = {} # key to PriorityNode mappings (denotes priority!)
        self.prioToNode = {}
        self.head = PriorityNode(0) # Dummy Node (similar to Deque problem yesterday)
        self.tail = PriorityNode(pow(10, 5)) # Dummy Node (similar to Deque problem yesterday)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        # Idea: Remove key from its current priority node. Add key to new priority node.
        # If old priority node is now empty (no keys), remove it from linked list.
        # If new priority node did not exist, add it to linked list.
        if key not in self.keyToNode:
            if 1 not in self.prioToNode:
                self.prioToNode[1] = PriorityNode(1)
                # H -> ... -> T
                # H -> node -> ... -> T
                node = self.prioToNode[1]
                old_first = self.head.next
                self.head.next = node
                node.next = old_first
                old_first.prev = node
                node.prev = self.head
            
            self.prioToNode[1].add(key)
            self.keyToNode[key] = self.prioToNode[1]
            return

        # First, remove key from its old node.
        node = self.keyToNode[key]
        node.remove(key)

        # Now, add it to new priority node (and create it if necessary)
        new_prio = node.priority + 1
        if new_prio not in self.prioToNode:
            self.prioToNode[new_prio] = PriorityNode(new_prio)
            # node.priority -> old_next
            # node.priority -> new_node -> old_next
            old_next = node.next
            new_node = self.prioToNode[new_prio]
            new_node.next = old_next
            old_next.prev = new_node
            new_node.prev = node
            node.next = new_node

        self.prioToNode[new_prio].add(key)
        self.keyToNode[key] = self.prioToNode[new_prio]
        # Now, if old node.priority is empty, node should be removed
        if node.isEmpty():
            # p -> node -> n
            # p -> n
            p, n = node.prev, node.next
            p.next = n
            n.prev = p
            del self.prioToNode[node.priority]
        
        return

    def dec(self, key: str) -> None:
        # Idea: Remove key from its current priority node. Add key to new priority node.
        # If old priority node is now empty (no keys), remove it from linked list.
        # If new priority node did not exist, add it to linked list.
        # assert key in self.keyToNode
        node = self.keyToNode[key]

        # First, remove key from its old node.
        node = self.keyToNode[key]
        node.remove(key)

        if node.priority == 1:
            del self.keyToNode[key]
            if not node.isEmpty():
                return
            
            # Delete PriorityNode 1 from head of list
            # assert self.head.next == node
            new_first = node.next
            self.head.next = new_first
            new_first.prev = self.head
            del self.prioToNode[node.priority]
            return

        # Now, add it to new priority node (and create it if necessary)
        new_prio = node.priority - 1
        if new_prio not in self.prioToNode:
            self.prioToNode[new_prio] = PriorityNode(new_prio)
            # old_prev -> node.priority
            # old_prev -> new_node -> node.priority
            old_prev = node.prev
            new_node = self.prioToNode[new_prio]
            old_prev.next = new_node
            new_node.next = node
            node.prev = new_node
            new_node.prev = old_prev
            
        self.prioToNode[new_prio].add(key)
        self.keyToNode[key] = self.prioToNode[new_prio]
        
        # Now, if old node.priority is empty, node should be removed
        if node.isEmpty():
            # p -> node -> n
            # p -> n
            p, n = node.prev, node.next
            p.next = n
            n.prev = p
            del self.prioToNode[node.priority]

        return

    def getMaxKey(self) -> str:
        # assert self.head.next is not None
        # assert self.tail.prev is not None
        if self.head.next == self.tail or self.tail.prev == self.head:
            # assert self.head.next == self.tail and self.tail.prev == self.head
            return ""
        
        # Get key from the lowest priority node
        node = self.tail.prev
        return node.getKey()

    def getMinKey(self) -> str:
        # assert self.head.next is not None
        # assert self.tail.prev is not None
        if self.head.next == self.tail or self.tail.prev == self.head:
            # assert self.head.next == self.tail and self.tail.prev == self.head
            return ""
        
        
        # Get key from the lowest priority node
        node = self.head.next
        return node.getKey()

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# MLQ/MLFQS:
# 64 []
# 63 []
# 62 []
# 61 []
# 60 [t1, t2]
# ...
# 4 []
# 3 [t3, t4,t5,t6]
# 2 [t7]
# 1 []

# All O` One:`
# H <-> 21 <-> 33 <-> 34 <-> 35 <-> 60 <-> T

# a b c
# 1 2 3 