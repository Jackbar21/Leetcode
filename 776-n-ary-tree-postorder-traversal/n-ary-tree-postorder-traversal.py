"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.res = []
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return root

        for node in root.children:
            self.postorder(node)
        # Once done with all children nodes, 
        # finally add root node to the array
        self.res.append(root.val)

        return self.res