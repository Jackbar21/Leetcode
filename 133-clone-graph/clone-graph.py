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
        original_value = node.val
        val_to_node = {}

        stack = [node]
        visited = set([node])
        while len(stack) > 0:
            original_node = stack.pop()
            val = original_node.val
            if val not in val_to_node:
                val_to_node[val] = Node(val)
            clone_node = val_to_node[val]

            for neighbor in original_node.neighbors:
                neighbor_val = neighbor.val
                if neighbor_val not in val_to_node:
                    val_to_node[neighbor_val] = Node(neighbor_val)
                clone_neighbor = val_to_node[neighbor_val]
                clone_node.neighbors.append(clone_neighbor)

                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)

        return val_to_node[original_value]
