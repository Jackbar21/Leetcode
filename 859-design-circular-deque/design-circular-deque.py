class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        # Case 1: List is empty
        if self.isEmpty():
            node = ListNode(value)
            self.head.next = node
            self.tail.prev = node
            self.size += 1
            return True

        node = ListNode(value)
        first_node = self.head.next

        node.next = first_node
        first_node.prev = node

        node.prev = self.head
        self.head.next = node
        
        self.size += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        # Case 1: List is empty
        if self.isEmpty():
            node = ListNode(value)
            self.head.next = node
            self.tail.prev = node
            self.size += 1
            return True
        
        node = ListNode(value)
        last_node = self.tail.prev

        last_node.next = node
        node.prev = last_node

        node.next = self.tail
        self.tail.prev = node
        
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        # Case 1: Only 1 Element
        if self.isSingle():
            self.head.next = None
            self.tail.prev = None
            self.size -= 1
            assert self.size == 0
            return True
        
        first_node = self.head.next
        second_node = first_node.next

        self.head.next = second_node
        second_node.prev = self.head
        
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        # Case 1: Only 1 Element
        if self.isSingle():
            self.head.next = None
            self.tail.prev = None
            self.size -= 1
            assert self.size == 0
            return True
        
        last_node = self.tail.prev
        second_last_node = last_node.prev
        
        self.tail.prev = second_last_node
        second_last_node.next = self.tail
        
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val

    def isEmpty(self) -> bool:
        assert 0 <= self.size <= self.capacity
        return self.size == 0

    def isFull(self) -> bool:
        assert 0 <= self.size <= self.capacity
        return self.size == self.capacity
    
    def isSingle(self) -> bool:
        assert 0 <= self.size <= self.capacity
        return self.size == 1

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()


# PREV SOLUTION:
# Uses collections.deque(), which I suppose is kind of considered "cheating" for this problem
# So I've reimplemented the Design Circular Deque without using collections.deque(), as I'm sure
# this problem likely intended.
"""
class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.deque = collections.deque([])
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.appendleft(value)
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.deque.append(value)
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.deque.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[0]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[-1]

    def isEmpty(self) -> bool:
        return len(self.deque) == 0
        

    def isFull(self) -> bool:
        return len(self.deque) == self.capacity
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
"""