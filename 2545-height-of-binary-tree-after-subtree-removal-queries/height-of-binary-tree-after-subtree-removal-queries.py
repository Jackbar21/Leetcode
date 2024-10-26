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
        # Precompute needed heights & depths metadata for each node, as well as
        # first & second biggest heights at each depth (needed for queries later!)
        self.populateHeights(root)
        self.populateDepths(root)

        # At this point, we now have access to:
        #   (1) value to height O(1) lookups
        #   (2) value to depth  O(1) lookups
        #   (3) depth to max_heap of each (-height, val) pair for each node at depth
        answer = []
        for val in queries:
            depth = self.num_to_depth[val]
            min_heap = self.depths[depth]
            # assert 1 <= len(min_heap) <= 2

            if len(min_heap) == 1:
                # depth - 1 is now maximum depth, and hence also new height of root
                answer.append(depth - 1)
                continue

            # In this case, min_heap is of length 2. Since this is a min-heap, 
            # the node with SMALLER height will be at index 0, and the one with
            # BIGGER (or equal) height will be at index 1.
            max_height, max_height_val = min_heap[1]
            second_max_height, _ = min_heap[0]

            if val == max_height_val:
                # Since val is the value with max height at current depth, it means
                # we're deleting the node with maximal height at this depth.
                # So we grab the second highest height at this depth, since new root height
                # will simply be this second highest height + its depth away from root node.
                answer.append(second_max_height + depth)
            else:
                # Answer is unchanged, since max height at depth remains intact :)
                answer.append(self.height[root.val])

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
                self.depths[depth] = []            
            min_heap = self.depths[depth]
            heapq.heappush(min_heap, (height, node.val))
            if len(min_heap) > 2:
                heapq.heappop(min_heap)
            
            # Loop Invariant
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
