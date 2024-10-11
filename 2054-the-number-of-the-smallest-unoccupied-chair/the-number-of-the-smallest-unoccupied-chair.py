class TreeNode:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.bst = None

    def initTree(self, l, r):
        if l >= r:
            return None if l > r else TreeNode(l)
        
        mid = (l + r) // 2
        root = TreeNode(mid)
        root.left = self.initTree(l, mid - 1)
        root.right = self.initTree(mid + 1, r)
        return root
    
    def insertTreeNode(self, val, root):
        if not root:
            # root = TreeNode(val)
            # return root
            return TreeNode(val)
        
        # assert val != root.val
        if val < root.val:
            root.left = self.insertTreeNode(val, root.left)
        else:
            root.right = self.insertTreeNode(val, root.right)
        
        return root
    
    def deleteTreeNode(self, val, root):
        # assert root is not None
        if val < root.val:
            root.left = self.deleteTreeNode(val, root.left)
            return root

        if val > root.val:
            root.right = self.deleteTreeNode(val, root.right)
            return root
        
        # assert val == root.val
        # Case 1: root.left == root.right == None
        if not root.left and not root.right:
            # root = None
            # return root
            return None

        # Case 2: root.left == None (i.e. root.right != None)
        if not root.left:
            # assert root.right
            # root = root.right
            # return root
            return root.right
        
        # Case 3: root.right == None (i.e. root.left != None)
        if not root.right:
            # assert root.left
            # root = root.left
            # return root
            return root.left

        # Case 4: root.left != None and root.right != None
        # Get next smallest element
        # assert root.left is not None and root.right is not None
        smallest_val = self.getSmallestVal(root.right)
        root.val = smallest_val
        root.right = self.deleteTreeNode(smallest_val, root.right)
        return root

    def getSmallestVal(self, root):
        # assert root is not None
        return root.val if not root.left else self.getSmallestVal(root.left)

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        self.bst = self.initTree(0, n - 1)

        # Idea: we know that if all friends have a chair, they'll only occupy the first
        # n chairs. Hence, we don't need to consider an infinite amount of chairs, but
        # rather the first n, as possible candidates for the next smallest chair each time.
        # We will use a BST that contains ALL available chairs at a point in time. When a
        # friend grabs a chair, it will be deleted from the BST (O(logn) w/ AVL tree), and
        # when a friend releases a chair, it will be added back into the BST (O(logn) w/ AVL tree)
        # to indicate that it is available once again. We can also grab the smallest avaialble
        # chair by doing a DFS from root to leftmost node (O(logn) w/ AVL tree). This should
        # theoretically allow us to solve the problem in O(nlogn) time w/ AVL tree, but technically
        # O(n^2) time when unlucky with BST. To minimize this inconvenience, the tree will be
        # initially balanced, but since I'm not writing a self-balancing tree algorithm, worst
        # case is still TECHNICALLY O(n^2)
    
        # arrival_times = collections.deque(sorted(map(lambda i: (times[i][0], i), range(n))))
        # leaving_times = collections.deque(sorted(map(lambda i: (times[i][1], i), range(n))))
        arrival_times = sorted(map(lambda i: (times[i][0], i), range(n)))
        leaving_times = sorted(map(lambda i: (times[i][1], i), range(n)))
        arrival_index, leaving_index = 0, 0
  
        taken = {} # friend to currently taken chair mappings
        while arrival_index < len(arrival_times) and leaving_index < len(leaving_times):
            next_arrival, friend_arrival = arrival_times[arrival_index]
            next_leaving, friend_leaving = leaving_times[leaving_index]
            #print(next_arrival < next_leaving)
            
            if next_arrival < next_leaving:
                # pass
                # Delete smallest from BST
                # and keep track that THIS FRIEND took THIS CHAIR
                # assert self.bst is not None
                smallest_val = self.getSmallestVal(self.bst) # i.e. smallest number chair
                if friend_arrival == targetFriend:
                    
                    return smallest_val
                # self.insertTreeNode(smallest_val, self.bst)

                # self.inorder(self.bst)
                #print("SA", smallest_val)
                self.bst = self.deleteTreeNode(smallest_val, self.bst)
                # self.inorder(self.bst)
                #print(" \n")
                # assert friend_arrival not in taken
                taken[friend_arrival] = smallest_val

                # IF the friend for next_arrival IS TARGET_FRIEND,
                # THEN RETURN THIS CHAIR VALUE!!!
                # arrival_times.popleft()
                arrival_index += 1
            else:
                # pass
                # Add leaving friend's chair back to BST
                # assert friend_leaving in taken
                val = taken[friend_leaving]
                self.bst = self.insertTreeNode(val, self.bst)
                del taken[friend_leaving]
                # leaving_times.popleft()
                leaving_index += 1


        # print(len(arrival_times))
        # print(len(leaving_times))

        return -1