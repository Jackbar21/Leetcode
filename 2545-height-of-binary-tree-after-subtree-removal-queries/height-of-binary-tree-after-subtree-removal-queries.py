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
    
    def populateAnswers(self, root, depth, case2):
        if not root:
            return
        
        # if root.val == self.root_val:
        #     if root.left:
        #         self.ans[root.left.val] = self.height[root.right] + 1
        #         self.populateAnswers(root.left, 1, True)
            
        #     if root.right:
        #         self.ans[root.right.val] = self.height[root.left] + 1
        #         self.populateAnswers(root.right, 1, False)

        #     return
        
        assert root.val != self.root_val
        
        # if not root.left and not root.right:
        #     return
        
        # if not root.left:
        #     self.ans[root.right.val] = 0
        #     self.populateAnswers(root.right)
        #     return
        
        # if not root.right:
        #     self.populateAnswers(root.left)
        #     return
        
        # If I delete the left child, answer is just right child's height + 1
        # And vice versa for deleting right child :)
        # assert root.left and root.right

        # case2 = None
        # if is_left:
        #     case2 = self.height[self.root.right] + 1
        # else:
        #     case2 = self.height[self.root.left] + 1
        
        if root.left:
            # self.ans[root.left.val] = self.height[root.right] + 1 + depth
            case1 = self.height[root.right] + 1 + depth

            self.ans[root.left.val] = max(case1, case2)
            print(f"{root.left.val}, {case1=}, {case2=}")
            # ADD distance from root to node as well!
            self.populateAnswers(root.left, depth + 1, case2)
        
        if root.right:
            # self.ans[root.right.val] = self.height[root.left] + depth
            case1 = self.height[root.left] + 1 + depth
            root_node = self.root
            
            self.ans[root.right.val] = max(case1, case2)
            print(f"{root.right.val}, {case1=}, {case2=}")
            # ADD distance from root to node as well!
            self.populateAnswers(root.right, depth + 1, case2)

    
    def isLeaf(self, node):
        return node and not node.left and not node.right

    def populateLeftNodes(self, left_root):
        if not left_root:
            return
        
        self.left_nodes.add(left_root)
        self.populateLeftNodes(left_root.left)
        self.populateLeftNodes(left_root.right)
        return

    def is_left(self, node):
        return node in self.left_nodes

    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # Idea: for each node, keep track of heights of both nodes below (can do so
        # using a hash-map/dictionary). Then write a getHeight function, which first
        # queries if a child has been deleted (whose effective height is then 0), to
        # calculate height as either 0 or the height stored inside of the hash-map in case
        # child is still alive
        
        self.root = root
        self.root_val = root.val
        self.populateParents(root, None)
        self.populateHeights(root) # Populates all the heights (via memoization)
        self.populateLeftNodes(root.left) # Only includes nodes in root.left subtree
        self.populateDepths(root)
        
        answer = []

        for val in queries:
            node = self.num_to_node[val]
            depth = self.num_to_depth[val]
            height = self.height[node]
            max_heap = self.depths[depth]
            if len(max_heap) == 1:
                assert max_heap[0] == (-height, val)
                answer.append(depth - 1)
                continue
            
            # Otherwise, if this is not max element, height is unchanged,
            # or if it IS max element, pop from heap, get newest max-height
            # at depth, append answer, push back to heap, continue
            assert (-height, val) in max_heap # TODO: REMOVE since O(n)!!!
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

        # print(self.depths)
        # return []
        # print(self.height)
        # print(self.num_to_node)
        # At this point, we now have access to O(1) lookups of:
        #   (1) node to height
        #   (2) value to node
        #   (3) node to parent node
        #   (4) self.is_left(node) that returns True if and only if node belongs in root.left
        # self.populateAnswers(root, 1, True)
        if root.left:
            self.ans[root.left.val] = self.height[root.right] + 1
            case2 = self.height[root.right] + 1
            self.populateAnswers(root.left, 1, case2)
        
        if root.right:
            self.ans[root.right.val] = self.height[root.left] + 1
            case2 = self.height[root.left] + 1
            self.populateAnswers(root.right, 1, case2)
        # self.populateAnswers(root.left, 1, True)
        # self.populateAnswers(root.right, 1, False)
        print(self.ans)
        # return []
        answer = [self.ans[val] for val in queries]
        return answer
        
        # return None
        # for i in range(1, n + 1):
        #     self.ans[i] = self.getModifiedHeight(i)
        # return None

        #           1
        #               5
        #             3         
        #           2   4

        
        # cache = {}
        # answer = []
        # for val in queries:
        #     if val in cache:
        #         answer.append(cache[val])
        #         continue
    
        #     left_height = self.height[root.left]
        #     right_height = self.height[root.right]

        #     node = self.getNodeFromVal(val)
        #     parent = self.getParent(node)
        #     sibling = parent.left if node != parent.left else parent.right
        #     parent_height = self.height[sibling] + 1
        #     if parent == root:
        #         answer.append(parent_height)
        #         continue
        #     diff = abs(self.height[parent] - parent_height) # total loss in height
        #     node_height = self.height[node]

        #     # if not self.isLeaf(node):
        #     #     node_height += 1

        #     print(f"{node.val=}, {node_height=}, {self.is_left(node)=}")
        #     print(f"{left_height=}, {right_height=}")
        #     print("")
        #     # if self.is_left(node):
        #     #     left_height -= node_height
        #     # else:
        #     #     right_height -= node_height
        #     if self.is_left(parent):
        #         left_height -= diff
        #     else:
        #         right_height -= diff
            
        #     height = max(left_height, right_height) + 1
        #     cache[val] = height
        #     answer.append(height)
        
        # return answer


        cache = {}
        # return []

        answer = []

        for val in queries:
            if val in cache:
                answer.append(cache[val])
                continue

            self.tmp_height = {} # Clear it first for every query
            node = self.getNodeFromVal(val)
            # path = [node.val]
            path = []
            self.tmp_height[node] = -1 # Same as None
            parent = self.getParent(node)
            is_done = False
            while parent:
                left_height = self.tmp_height[parent.left] if parent.left in self.tmp_height else self.height[parent.left]
                right_height = self.tmp_height[parent.right] if parent.right in self.tmp_height else self.height[parent.right]

                height = max(left_height, right_height) + 1
                self.tmp_height[parent] = height
                # If no change, then there will be no further change
                # to remaining parents either, so can break out of the loop here
                if height == self.height[parent]:
                    break
                
                if (parent, height) in cache:
                    ans = cache[(parent, height)]
                    cache[val] = ans
                    is_done = True
                    answer.append(ans)
                    break
                else:
                    path.append((parent, height))

                # Loop Invariant
                # path.append(parent.val)
                parent = self.getParent(parent)
            
            if is_done:
                continue
            # assert root in self.tmp_height
            # ans = self.tmp_height[root]
            ans = self.tmp_height[root] if root in self.tmp_height else self.height[root]
            for (parent, height) in path:
                cache[(parent, height)] = ans
            cache[val] = ans
            answer.append(ans)

            # for node_val in path:
            #     cache[node_val] = ans
        
        return answer
                



        #     if not self.isDeleted(node):
        #         self.deleteNode(node)
            
        #     ans = self.getHeight(root)
        #     answer.append(ans)

        # return answer
        # return self.answer
    
    def deleteNode(self, node):
        # Firstly, mark node as deleted
        self.markDeleted(node)

        # Update all of the parents heights
        parent = self.getParent(node)
        while parent:
            self.height[parent] = self.getHeight(parent)

            # Loop Invariant
            parent = self.getParent(parent)
        
        return
    
    def getNodeFromVal(self, val):
        assert val in self.num_to_node
        return self.num_to_node[val]
    
    def markDeleted(self, node):
        assert not self.isDeleted(node)

        # Be lazy, and DO NOT waste time trying to delete subtree from current node
        # BUT, later on when deleting another node, it COULD have been a node we wanted
        # to already delete, so we should check each time if ANY of its parents have
        # already been deleted. If so, we can mark this node as DELETED (as well as any
        # node along its path if we so choose...), and return the same height that was
        # returned in the previous iteration (i.e. at answer[-1] so far...) :)

        # Step 1: mark node as deleted
        self.deleted.add(node)
    
    def isDeleted(self, node):
        if node in self.deleted:
            return True
        
        path = []
        # Eventually, node will become None, since None is parent of root :)
        while node:
            if node in self.deleted:
                # mark all nodes in path as deleted first,
                # then return True :)
                for path_node in path:
                    self.markDeleted(path_node) # TODO: update this maybe
                return True
            
            # Loop Invariant
            node = self.getParent(node)
        
        return False
        
    def getParent(self, node):
        assert node in self.parent
        return self.parent[node]
    
    def getHeight(self, node):
        left_height = -1
        right_height = -1

        # Only query left node height if it hasn't been deleted
        if not self.isDeleted(node.left):
            left_height = self.height[node.left]
        
        # Only query right node height if it hasn't been deleted
        if not self.isDeleted(node.right):
            right_height = self.height[node.right]
        
        return max(left_height, right_height) + 1
    
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
        
        assert root not in self.parent
        # self.parent[root.val] = parent.val if parent else -1
        self.parent[root] = parent

        self.populateParents(root.left, root)
        self.populateParents(root.right, root)

        

        return


#                   4
#          1                H=4
#      5        8           H=3
# H=40     H=90   H=21      H=2
