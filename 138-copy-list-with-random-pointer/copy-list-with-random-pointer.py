"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # I'm going to assume, from the problem description, that [val, random_index]
        # is enough to UNIQUELY determine a node in the linked list.
        if not head:
            return None

        node_to_index = {}
        index_to_node = {}
        index = 0

        cur_node = head
        while cur_node:
            node_to_index[cur_node] = index
            index_to_node[index] = cur_node

            # Loop Invariant
            cur_node = cur_node.next
            index += 1
        
        # Also consider None at end of list!
        node_to_index[None] = index
        index_to_node[index] = None
        
        # Idea: Build a new list of nodes, and put them into an index-able array.
        # Initially, they will only contain their values, and their 'next' and
        # 'random' pointers will be set to null/None. Then, once each node has
        # been created, we can begin assigning next and random pointers via the
        # new nodes indices in the array (keeping original order of initial linked list),
        # and then return the node at index 0 (the new head) to complete the problem.

        # Step 1: Build linked list in original order with JUST the values.
        count = index
        arr = []
        for i in range(count):
            node = index_to_node[i]
            # arr.append(Node(node.val, None, None))
            copy_node = Node(node.val)
            arr.append(copy_node)
        arr.append(None)

        # For each node in the list (except None at the end of course),
        # set its 'next' and 'random' pointer values as is appropriate.
        for i in range(len(arr) - 1):
            node = arr[i]
            node.next = arr[i + 1]

            # Our current node as at index i of arr. This means that its random
            # pointer should follow in respect to the node at the same index i
            # of the original linked list's random pointer. Since we have the
            # ability to map indices to nodes and nodes to indices, we can achieve this
            # by grabbing the node at index i of the original linnked list, getting
            # that original nodes random node, and then getting that random node from
            # the original linked list's index, and using that index to map the current
            # node's random pointer to the copied-node at that same index value in arr.
            original_node = index_to_node[i]
            random_node = original_node.random
            random_index = node_to_index[random_node]
            
            node.random = arr[random_index]
        
        return arr[0]

