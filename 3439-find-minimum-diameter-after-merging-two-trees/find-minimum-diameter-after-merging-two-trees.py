class TreeNode:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.children = set()

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        # We NEED to build the tree for both tree1 and tree2. We can define the root node as the
        # node with the smallest degree for either tree. Then, once this is done, we need to find
        # the SMALLEST diamater of EACH tree. The result then, will simply be the sum of these
        # two diameters, and +1 for the edge connected in between :)
        root1 = self.buildTree(edges1)
        root2 = self.buildTree(edges2)

        max_diam1 = self.getMaxDiameterInTree(root1)
        max_diam2 = self.getMaxDiameterInTree(root2)
        # print(f"{max_diam1=}, {max_diam2=}")
        # return -1
        res = math.ceil(max_diam1/2) + math.ceil(max_diam2/2) + 1
        res = max(res, max_diam1)
        res = max(res, max_diam2)
        return res

        # Idea: We want min diameter in each tree. We should compute the max diameter that goes
        # through a node, for every node in a tree... and then take the smallest of these in
        # the end!
    
    # def getDiameter(self, root):

    
    # WORKING FUNCTION!!!
    def getMaxDiameterInTree(self, root):
        res = self.getDiameterFromNode(root)
        for child in root.children:
            res = max(res, self.getMaxDiameterInTree(child))
        return res
    

    # WORKING FUNCTION!!!
    def getDiameterFromNode(self, node):
        # return max(self.getDepth(node), self.getHeight(node))
        # res = self.getDepth(node)
        # for child in node.children:
        #     res = max(res, )

        # case2 = max([1 + self.getHeight(child) for child in node.children], default = 0)
        # return max(case1, case2)

        # The diameter of a node will be the sum of the heights of the two children
        # with the largest heights. If there are less than two children, it's easy:
        # 0 Children <==> Diameter of 1,
        # 1 Child <==> Height of the single child!
        if len(node.children) == 0:
            return 0
        
        if len(node.children) == 1:
            return 1 + self.getHeight(list(node.children)[0])
        
        # Otherwise, need to grab two largest heights! We can do this via two O(n)
        # parsings, instead of sorting which takes O(nlogn) :P
        return 2 + sum(sorted(self.getHeight(child) for child in node.children)[-2:])
        max_child, max_height = None, float("-inf")
        for child in node.children:
            child_height = self.getHeight(child)
            if child_height > max_height:
                max_child = child
                max_height = child_height
        
        second_max_height = float("-inf")
        for child in node.children:
            child_height = self.getHeight(child)
            if child_height > second_max_height and child != max_child:
                second_max_height = child_height
        
        return 2 + max_height + second_max_height

    @cache
    def getHeight(self, node):
        if len(node.children) == 0:
            return 0
        return 1 + max(self.getHeight(child) for child in node.children)

    
    def buildTree(self, edges):
        # Step 1: Build an adjacency list, and get the degrees of each node.
        # REMEMBER... this is an UNDIRECTED graph!
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        root_val = random.randint(0, len(edges)) # Pick any node as root!
        root = TreeNode(root_val)

        # Now, this will be the root node, so we will make the relationships NO LONGER
        # UNDIRECTED!!! I.e., we need to give each node direct children, and differentiate
        # their old bi-directional relationships into direct parent-to-child relationships!
        visited_vals = set() # Tree is built once all N nodes have been placed into the tree!
        visited_vals.add(root_val)
        queue = collections.deque([root])
        while len(queue) > 0:
            node = queue.popleft()
            node_val = node.val
            for neighbor_val in adj_list[node_val]:
                if neighbor_val in visited_vals:
                    continue
                visited_vals.add(neighbor_val)
                neighbor_node = TreeNode(neighbor_val)
                queue.append(neighbor_node)
                node.children.add(neighbor_node)

        return root
            

# 1 <-> 2 <-> 3 <-> 0


# 0->1
#  \
#   4

#  1   4
#   \ /
# 8->0->2->7->6->3->5
#  \
#   9