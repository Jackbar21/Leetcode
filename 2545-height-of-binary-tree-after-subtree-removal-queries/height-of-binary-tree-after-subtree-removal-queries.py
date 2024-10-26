# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.height = {}
        self.depths = {}
        self.num_to_depth = {}

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Idea: for each node, keep track of heights of both nodes below (can do so
        # using a hash-map/dictionary). Then write a getHeight function, which first
        # queries if a child has been deleted (whose effective height is then 0), to
        # calculate height as either 0 or the height stored inside of the hash-map in case
        # child is still alive
        
   
        self.populateHeights(root)
        self.populateDepths(root)

        # At this point, we now have access to:
        #   (1) value to height O(1) lookups
        #   (2) value to depth  O(1) lookups
        #   (3) depth to max_heap of each (-height, val) pair for each node at depth
        
        HEIGHT, VAL = 0, 1
        answer = []
        for val in queries:
            depth = self.num_to_depth[val]
            max_heap = self.depths[depth]

            if len(max_heap) == 1:
                # depth - 1 is now maximum depth, and hence also new height of root
                answer.append(depth - 1)
                continue

            if max_heap[0][VAL] != val:
                # Answer is unchanged
                answer.append(self.height[root.val])
                continue
            
            # We're deleting node with maximal height at this depth
            # So get second highest height at this depth, since new root height
            # will simply be this second highest height + its depth away from root node
            tmp = heapq.heappop(max_heap)
            height = -max_heap[0][HEIGHT] # negative since simulating max-heap via min-heap
            answer.append(height + depth)
            heapq.heappush(max_heap, tmp)

        return answer
    
    def populateHeights(self, root):
        if not root:
            return
        
        # Important to do POSTORDER traversal, that way ALWAYS
        # have access to left and right children's heights FIRST!
        self.populateHeights(root.left)
        self.populateHeights(root.right)

        # NOW, we have access to left and right childrens heights :)
        left_height = -1 if not root.left else self.height[root.left.val]
        right_height = -1 if not root.right else self.height[root.right.val]

        height = max(left_height, right_height) + 1
        self.height[root.val] = height

    def populateDepths(self, root):
        stack = [(root, 0)] # (node, depth) pairs

        while len(stack) > 0:
            node, depth = stack.pop()
            height = self.height[node.val]

            # Update depths metadata
            self.num_to_depth[node.val] = depth
            if depth not in self.depths:
                self.depths[depth] = [(-height, node.val)]
            else:
                heapq.heappush(self.depths[depth], (-height, node.val))
            
            # Loop Invariant
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
            

#                   4
#          1                H=4
#      5        8           H=3
# H=40     H=90   H=21      H=2
