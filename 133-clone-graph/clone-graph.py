"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        val_to_node = {
            val: Node(val) for val in range(0, 100 + 1)
        }
        
        # if node is not None:
        #     print(f"{node.val=}, {node.neighbors=}")
        # return node

        # I will need to perform two traversals of this graph. One time to populate
        # all of the cloned nodes, and another time to populate all the appropriate neighbors!

        # Step 1: 

        # Step 2: Populate all the neighbors!
        queue = collections.deque([node])
        visited = set([node])
        while len(queue) > 0:
            original_node = queue.popleft()
            clone_node = val_to_node[original_node.val]

            for neighbor in original_node.neighbors:
                clone_node.neighbors.append(val_to_node[neighbor.val])
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return val_to_node[1]
