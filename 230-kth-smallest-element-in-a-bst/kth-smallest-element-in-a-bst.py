# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Idea: Simply do an inorder traversal from root, and return the k'th visited node's value!
        # CHALLENGE: I'm gonna force myself to do this iteratively >:)

        stack = [root]
        nodes_visited = 0
        while len(stack) > 0:
            node = stack.pop()
            left_node = node.left
            if left_node:
                # To allow for termination! 
                # Another way to do this without modifying the tree
                # would be by using a hash-set for one-time lookups :)
                node.left = None 
        
                stack.append(node)
                stack.append(left_node)
                continue

            # Inorder traversal!
            assert not left_node

            nodes_visited += 1
            if nodes_visited == k:
                return node.val
            
            if node.right:
                stack.append(node.right)
        
        return -1
