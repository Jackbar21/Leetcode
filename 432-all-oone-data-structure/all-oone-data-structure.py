class PriorityNode:
    def __init__(self, priority = 0):
        self.priority = priority
        self.next = None
        self.prev = None
        # self.nextPriority = None
        self.keys = set()
    def add(self, key):
        self.keys.add(key)
    def remove(self, key):
        ##print(f"remove: {self.__str__()}")
        assert key in self.keys
        self.keys.remove(key)
    def isEmpty(self):
        return len(self.keys) == 0
    def getKey(self):
        assert not self.isEmpty()
        key = self.keys.pop()
        self.add(key)
        return key
    def __str__(self):
        return f"prio={self.priority}, keys={self.keys}, prev={self.prev.priority if self.prev else None}, next={self.next.priority if self.next else None}"

class AllOne:
    def llToList(self):
        cur = self.head.next
        res = []
        while cur != self.tail:
            res.append(str(cur))
            cur = cur.next
        return res
    def __init__(self):
        self.keyToNode = {} # key to PriorityNode mappings (denotes priority!)
        # self.prioToNode = {0: PriorityNode(0)}
        self.prioToNode = {}
        self.head = PriorityNode(0) # Dummy Node (similar to Deque problem yesterday)
        self.tail = PriorityNode(pow(10, 5)) # Dummy Node (similar to Deque problem yesterday)
        self.head.next = self.tail
        self.tail.prev = self.head
        # self.head = PriorityNode(0) # Priority 0 should always be empty (Dummy Node)
        # self.lowest_prio = float("inf")
        # self.highest_prio = float("-inf")
        # ##print("__init__", {key: self.prioToNode[key] for key in self.prioToNode}, {key: self.keyToNode[key] for key in self.keyToNode}, self.lowest_prio, self.highest_prio, "\n")
        
        # self.min_heap = []
        # self.max_heap = [] # w/ a min_heap, just use negative values instead!

        # 1 -> 4 -> 89
        
        #               H
        # 1 2 3 4 5 6 7 8 9 10
        # 1 1 1 1 2 1 1 1 1 3 3 3 3

    def inc(self, key: str) -> None:
        ##print(self.llToList(), key, "inc")
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
                
            
            # #print("INC-INIT", self.llToList())

            
            
            self.prioToNode[1].add(key)
            self.keyToNode[key] = self.prioToNode[1]
            # #print(f"INC-1, {str(old_prev)=}, {str(node)=}, {str(new_node)=}, {str(old_next)=}")
            ##print(self.llToList(), key, "inc-ret-1", "\n")
            # #print("INC-INIT-END", self.llToList())
            # #print
            return

        # First, remove key from its old node.
        node = self.keyToNode[key]
        # ##print(self.llToList())
        node.remove(key)

        # Now, add it to new priority node (and create it if necessary)
        new_prio = node.priority + 1
        if new_prio not in self.prioToNode:
            self.prioToNode[new_prio] = PriorityNode(new_prio)
            # node.priority -> old_next
            # node.priority -> new_node -> old_next

            # old_prev -> node -> old_next
            # old_prev -> node -> new_node -> old_next
            old_prev = node.prev
            old_next = node.next
            new_node = self.prioToNode[new_prio]
            new_node.next = old_next
            old_next.prev = new_node
            new_node.prev = node
            node.next = new_node
            #print(f"INC-2, {str(old_prev)=}, {str(node)=}, {str(new_node)=}, {str(old_next)=}")
        self.prioToNode[new_prio].add(key)
        self.keyToNode[key] = self.prioToNode[new_prio]
        # Now, if old node.priority is now empty, node should be removed
        if node.isEmpty():
            # p -> node -> n
            # p -> n
            p, n = node.prev, node.next
            p.next = n
            n.prev = p
            del self.prioToNode[node.priority]
        
        ##print(self.llToList(), key, "inc-ret-2", "\n")
        return




        # # self.priority[key] = self.priority.get(key, 0) + 1
        # if key not in self.keyToNode:
        #     if 1 not in self.prioToNode:
        #         self.prioToNode[1] = PriorityNode(1)
        #     self.prioToNode[1].add(key)
        #     self.keyToNode[key] = self.prioToNode[1]
        #     if self.lowest_prio != float("inf") and self.lowest_prio > 1:
        #         # assert self.lowest_prio != 1
        #         self.prioToNode[1].next = self.prioToNode[self.lowest_prio]
        #     self.lowest_prio = min(self.lowest_prio, 1)
        #     self.highest_prio = max(self.highest_prio, 1)
        #     ##print("inc1", {key: str(self.prioToNode[key]) for key in self.prioToNode}, {key: str(self.keyToNode[key]) for key in self.keyToNode}, self.lowest_prio, self.highest_prio, "\n")
            
                
        #     return

        # # Delete from current PriorityNode
        # node = self.keyToNode[key]
        # ##print(node, key)
        # node.remove(key)
        # # if node.IsEmpty():
        # new_prio = node.priority + 1
        # self.highest_prio = max(self.highest_prio, new_prio)
        # if new_prio not in self.prioToNode:
        #     self.prioToNode[new_prio] = PriorityNode(new_prio)
        #     # Case
        #     # next_node = node.next
        #     # self.prioToNode[new_prio].next = next_node
        #     # if next_node:
        #     #     next_node.prev = self.prioToNode[new_prio]

        #     # node.next = self.prioToNode[new_prio]
        #     # self.prioToNode[new_prio] = node

        # self.prioToNode[new_prio].add(key)
        # self.keyToNode[key] = self.prioToNode[new_prio]
        # next_node = node.next
        # self.prioToNode[new_prio].next = next_node
        # if next_node:
        #     next_node.prev = self.prioToNode[new_prio]

        # node.next = self.prioToNode[new_prio]
        # self.prioToNode[new_prio] = node
        # # self.prioToNode[new_prio].next = node.next
        # # node.next = self.prioToNode[new_prio]

        # if node.isEmpty():
        #     if self.lowest_prio == node.priority:
        #         self.lowest_prio += 1
        #     del self.prioToNode[node.priority]
        
        # ##print(node)
        # ##print("inc2", {key: self.prioToNode[key] for key in self.prioToNode}, {key: self.keyToNode[key] for key in self.keyToNode}, self.lowest_prio, self.highest_prio, "\n")
        
            
        # return

        
        
        
            

        



        # # cur_max, cur_key = self.max
        # # if self.priority[key] > cur_max:
        # # heapq.heappush(self.min_heap, (self.priority[key], key))
        # # heapq.heappush(self.max_heap, (-self.priority[key], key))

    def dec(self, key: str) -> None:
        ##print(self.llToList(), key, "dec")
        # Idea: Remove key from its current priority node. Add key to new priority node.
        # If old priority node is now empty (no keys), remove it from linked list.
        # If new priority node did not exist, add it to linked list.
        assert key in self.keyToNode
        node = self.keyToNode[key]

        # if key not in self.keyToNode:
        #     if 1 not in self.prioToNode:
        #         self.prioToNode[1] = PriorityNode(1)
            
        #     # H -> ... -> T
        #     # H -> node -> ... -> T
        #     node = self.prioToNode[1]
        #     old_first = head.next
        #     head.next = node
        #     node.next = old_first
        #     old_first.prev = node
        #     node.prev = head
        #     self.keyToNode[key] = self.prioToNode[1]
        #     return

        # First, remove key from its old node.
        node = self.keyToNode[key]
        # ##print(self.llToList())
        node.remove(key)

        if node.priority == 1:
            del self.keyToNode[key]
            # TODO: implement logic for this case

            # head -> 1 -> 89 -> ... -> tail
            # Case 1: node is empty
            # Case 2: node is not empty
            # If PriorityNode with priority == 1 is empty
            # after removing key, then it must be deleted
            # from head of linked list, with new head pointing
            # to second lowest PriorityNode, which by our linked list
            # structure, w
            if not node.isEmpty():
                ##print(self.llToList(), key, "dec-ret-notempty", "\n")
                return
            
            # Delete PriorityNode 1 from head of list
            # ##print("DSA")
            # ##print(self.llToList(), str(node))
            assert self.head.next == node
            new_first = node.next
            self.head.next = new_first
            new_first.prev = self.head
            del self.prioToNode[node.priority]

            # Delete node data from keyToNode and prioToNode hash-maps as well
            # del self.keyToNode[key]
            # del self.prioToNode[1]
            
            ##print(self.llToList(), key, "dec-ret-1", "\n")
            return
            assert False

        # Now, add it to new priority node (and create it if necessary)
        new_prio = node.priority - 1
        # ##print({key: str(self.prioToNode[key]) for key in self.prioToNode}, new_prio)
        if new_prio not in self.prioToNode:
            self.prioToNode[new_prio] = PriorityNode(new_prio)
            # old_prev -> node.priority
            # old_prev -> new_node -> node.priority
            old_next = node.next
            old_prev = node.prev
            new_node = self.prioToNode[new_prio]
            old_prev.next = new_node
            new_node.next = node
            node.prev = new_node
            new_node.prev = old_prev
            #print(f"DEC-2, {str(old_prev)=}, {str(node)=}, {str(new_node)=}, {str(old_next)=}")
            # new_node.prev = old_prev
            # node.prev = new_node
            # new_node.next = node
            
            ##print(self.llToList(), key, "dec-add")
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
        
        # self.keyToNode[key] = self.prioToNode[new_prio]
        ##print(self.llToList(), key, "dec-ret-2", "\n")
        return

        # assert key in self.priority
        # self.priority[key] -= 1
        # if self.priority[key] == 0:
        #     del self.priority[key]
        #     return

        # if key not in self.keyToNode:
        #     if 1 not in self.prioToNode:
        #         self.prioToNode[1] = PriorityNode(1)
        #     self.prioToNode[1].add(key)
        #     self.keyToNode[key] = self.prioToNode[1]
        #     self.lowest_prio = min(self.lowest_prio, 1)
        #     self.highest_prio = max(self.highest_prio, 1)
        #     return
        assert key in self.keyToNode

        # Delete from current PriorityNode
        node = self.keyToNode[key]
        ##print(self.llToList())
        node.remove(key)
        # if node.IsEmpty():
        new_prio = node.priority - 1
        if new_prio != 0:
            # self.highest_prio = max(self.highest_prio, new_prio)
            self.lowest_prio = min(self.lowest_prio, new_prio)
            if new_prio not in self.prioToNode:
                self.prioToNode[new_prio] = PriorityNode(new_prio)
                # Case
                # next_node = node.next if node.isEmpty() else node
                # self.prioToNode[new_prio].next = next_node
                # next_node.prev = self.prioToNode[new_prio]
                # node.next = self.prioToNode[new_prio]

            self.prioToNode[new_prio].add(key)
            self.keyToNode[key] = self.prioToNode[new_prio]
            next_node = node.next if node.isEmpty() else node
            self.prioToNode[new_prio].next = next_node
            next_node.prev = self.prioToNode[new_prio]
            # 1 -> ... -> 3 -> 4 -> ... 89
            # self.prioToNode[new_prio].next = node.next if node.isEmpty() else node
            # node.next = self.prioToNode[new_prio]

            if node.isEmpty():
                # if self.lowest_prio == node.priority:
                #     self.lowest_prio += 1
                if self.highest_prio == node.priority:
                    self.highest_prio -= 1
                del self.prioToNode[node.priority]
            
            ##print("dec1 "+key, {key: self.prioToNode[key] for key in self.prioToNode}, {key: self.keyToNode[key] for key in self.keyToNode}, self.lowest_prio, self.highest_prio, "\n")
            
                
            return
        
        # assert new_prio == 0
        # We are about to delete priority node 1
        assert node.priority == 1 and new_prio == 0
        # del self.keyToNode[key]
        if not node.isEmpty():
            ##print("dec2 " +key, {key: self.prioToNode[key] for key in self.prioToNode}, {key: self.keyToNode[key] for key in self.keyToNode}, self.lowest_prio, self.highest_prio, "\n")
            
                
            del self.keyToNode[key]
            return
        

        self.lowest_prio = node.next.priority if node.next else float("inf")
        self.highest_prio = self.highest_prio if node.next else float("-inf")

        del self.prioToNode[1]
        ##print("dec3 "+key, {key: self.prioToNode[key] for key in self.prioToNode}, {key: self.keyToNode[key] for key in self.keyToNode}, self.lowest_prio, self.highest_prio, "\n")
        
            
        del self.keyToNode[key]




        # # assert key in self.priority
        # self.priority[key] -= 1
        # if self.priority[key] == 0:
        #     del self.priority[key]
        #     return
        
        # heapq.heappush(self.min_heap, (self.priority[key], key))
        # heapq.heappush(self.max_heap, (-self.priority[key], key))

    def getMaxKey(self) -> str:
        # #print(self.llToList(), "getMaxKey", "\n")
        #print("getMaxKey", {prio: str(self.prioToNode[prio]) for prio in self.prioToNode})

        assert self.head.next is not None
        assert self.tail.prev is not None
        if self.head.next == self.tail or self.tail.prev == self.head:
            assert self.head.next == self.tail and self.tail.prev == self.head
            return ""
        
        # Pop a key from the lowest priority node
        # #print(self.llToList())
        # #print(self.head, self.tail)
        #print(f"{str(self.head)=}, {str(self.tail)=}")
        node = self.tail.prev
        key = node.getKey()
        #print(key)
        return key
        return self.head.next

        if self.highest_prio == float("-inf"):
            return ""
        prio = self.highest_prio
        node = self.prioToNode[prio]
        ##print("getMaxKey", {key: self.prioToNode[key] for key in self.prioToNode}, {key: self.keyToNode[key] for key in self.keyToNode}, self.lowest_prio, self.highest_prio, "\n")
        
            
        # self.highest_prio
        key = node.keys.pop()
        node.add(key)
        return key

        if len(self.priority) == 0:
            return ""
        
        # val, key = self.max_heap[0]
        # while self.priority.get(key, 0) != -val:
        #     heapq.heappop(self.max_heap)
        #     val, key = self.max_heap[0]

        # return key

    def getMinKey(self) -> str:
        # #print(self.llToList(), "getMinKey", "\n")
        #print("getMinKey", {prio: str(self.prioToNode[prio]) for prio in self.prioToNode})
        assert self.head.next is not None
        assert self.tail.prev is not None
        if self.head.next == self.tail or self.tail.prev == self.head:
            assert self.head.next == self.tail and self.tail.prev == self.head
            #print(self.llToList())
            return ""
        
        # head -> 1 -> 2 -> 4 -> 79 -> tail
        
        # Pop a key from the lowest priority node
        node = self.head.next
        key = node.getKey()
        #print(key)
        #print(self.llToList())
        return key


        if self.lowest_prio == float("inf"):
            return ""
        prio = self.lowest_prio
        node = self.prioToNode[prio]
        ##print("getMinKey", {key: self.prioToNode[key] for key in self.prioToNode}, {key: self.keyToNode[key] for key in self.keyToNode}, self.lowest_prio, self.highest_prio, "\n")
        
            
        key = node.keys.pop()
        node.add(key)
        return key


        if len(self.priority) == 0:
            return ""
        
        # val, key = self.min_heap[0]
        # while self.priority.get(key, 0) != val:
        #     heapq.heappop(self.min_heap)
        #     val, key = self.min_heap[0]

        # return key

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()