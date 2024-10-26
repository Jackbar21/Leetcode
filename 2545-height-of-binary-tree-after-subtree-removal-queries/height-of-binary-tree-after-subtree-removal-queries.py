# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.parent = {} # node to parent node (None for root)
        self.height = {None: -1} # That way leaf node height == max(-1, -1) + 1 == 0, as wanted
        self.num_to_node = {}
        self.left_nodes = set() # Contains only nodes that are inside root.left subtree
        self.deleted = set()
        self.tmp_height = {None: -1}
        self.ans = {} # answer to queries[i] for each i, where 1 <= i <= n
        self.root_val = None
        self.root = None
        self.depths = {}
        self.num_to_depth = {}

        # self.answer = []
    
    def populateDepths(self, root, depth = 0):
        if not root:
            return
        
        self.num_to_depth[root.val] = depth
        
        if depth not in self.depths:
            self.depths[depth] = []
        height = self.height[root]
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
        self.populateParents(root, None)
        self.populateHeights(root) # Populates all the heights (via memoization)
        # self.populateLeftNodes(root.left) # Only includes nodes in root.left subtree
        self.populateDepths(root)

        # At this point, we now have access to O(1) lookups of:
        #   (1) node to height
        #   (2) value to node
        #   (3) node to parent node
        #   (4) self.is_left(node) that returns True if and only if node belongs in root.left
        
        answer = []
        for val in queries:
            node = self.num_to_node[val]
            depth = self.num_to_depth[val]
            height = self.height[node]
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
                answer.append(self.height[root])
                continue
            
            # REMEMBER TO ADD ITEM BACK!!!
            item = heapq.heappop(max_heap)

            h, v = max_heap[0]
            h = -h
            answer.append(h + depth)

            heapq.heappush(max_heap, item)

        return answer
    
    def getNodeFromVal(self, val):
        # assert val in self.num_to_node
        return self.num_to_node[val]
    
   
    def getParent(self, node):
        # assert node in self.parent
        return self.parent[node]
    
    def populateHeights(self, root):
        if root in self.height:
            return self.height[root]
        
        left_height = self.populateHeights(root.left)
        right_height = self.populateHeights(root.right)

        height = max(left_height, right_height) + 1
        self.height[root] = height
        return height
        
    def populateParents(self, root, parent):
        if not root:
            return
        
        # Map root.val to root for easy query-lookups later on :)
        # (This breaks S in SOLID, please don't murder me Rawad...)
        self.num_to_node[root.val] = root
        
        # assert root not in self.parent
        # self.parent[root.val] = parent.val if parent else -1
        self.parent[root] = parent

        self.populateParents(root.left, root)
        self.populateParents(root.right, root)

        

        return


#                   4
#          1                H=4
#      5        8           H=3
# H=40     H=90   H=21      H=2
