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

    def populateDepths(self, root, depth = 0):
        if not root:
            return
        
        self.num_to_depth[root.val] = depth
        
        if depth not in self.depths:
            self.depths[depth] = []
        height = self.height[root.val]
        heapq.heappush(self.depths[depth], (-height, root.val))

        self.populateDepths(root.left, depth + 1)
        self.populateDepths(root.right, depth + 1)

        return

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Idea: for each node, keep track of heights of both nodes below (can do so
        # using a hash-map/dictionary). Then write a getHeight function, which first
        # queries if a child has been deleted (whose effective height is then 0), to
        # calculate height as either 0 or the height stored inside of the hash-map in case
        # child is still alive
        
        # self.root = root
        # self.root_val = root.val
        # self.populateParents(root, None)
        self.getHeight(root) # Populates all the heights (via memoization)
        # self.populateLeftNodes(root.left) # Only includes nodes in root.left subtree
        self.populateDepths(root)

        # At this point, we now have access to O(1) lookups of:
        #   (1) node to height
        #   (2) value to node
        #   (3) node to parent node
        #   (4) self.is_left(node) that returns True if and only if node belongs in root.left
        
        answer = []
        for val in queries:
            # node = self.num_to_node[val]
            depth = self.num_to_depth[val]
            height = self.height[val]
            max_heap = self.depths[depth]
            if len(max_heap) == 1:
                # assert max_heap[0] == (-height, val)
                answer.append(depth - 1)
                continue
            
            # Otherwise, if this is not max element, height is unchanged,
            # or if it IS max element, pop from heap, get newest max-height
            # at depth, append answer, push back to heap, continue
            # # assert (-height, val) in max_heap # TODO: REMOVE since O(n)!!!

            if max_heap[0] != (-height, val):
                # Answer is unchanged
                answer.append(self.height[root.val])
                continue
            
            # REMEMBER TO ADD ITEM BACK!!!
            item = heapq.heappop(max_heap)

            h, v = max_heap[0]
            h = -h
            answer.append(h + depth)

            heapq.heappush(max_heap, item)

        return answer

    def getHeight(self, root):
        if not root:
            # That way leaf node height == max(-1, -1) + 1 == 0, as wanted
            return -1

        if root.val in self.height:
            return self.height[root.val]
        
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)

        height = max(left_height, right_height) + 1
        self.height[root.val] = height
        return height
        

#                   4
#          1                H=4
#      5        8           H=3
# H=40     H=90   H=21      H=2
