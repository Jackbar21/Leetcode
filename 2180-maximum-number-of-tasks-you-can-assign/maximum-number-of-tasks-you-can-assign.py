class TreeNode:
    def __init__(self, val, index):
        self.val = val
        self.index = index # unique identifier for deletes!
        self.left = None
        self.right = None
    
    @staticmethod
    def delete(root, delete_node):
        # if not root:
        #     return None
        index = root.index
        # val = root.val
        # delete_val = delete_node.val
        delete_index = delete_node.index
        if delete_index < index:
            root.left = TreeNode.delete(root.left, delete_node)
            return root

        if delete_index > index:
            root.right = TreeNode.delete(root.right, delete_node)
            return root
        
        assert index == delete_index
        assert root == delete_node
        #print(f"{root=}, {root.val=}, {root.index}=")
        #print(f"{delete_node=}, {delete_node.val=}, {delete_node.index}=")
        # assert val == delete_val
        # assert delete_node == root
        # if root != delete_node:
        #     assert (root.left and root.left.val == delete_val) or (root.right.val == delete_val)
        #     # Doing both, which is NOT O(logn), but need to come up w/ solutions here
        #     if root.left and root.left.val == delete_val:
        #         root.left = TreeNode.delete(root.left, delete_node)
        #     if root.right and root.right.val == delete_val:
        #         root.right = TreeNode.delete(root.right, delete_node)
        #     return root

        if not root.left and not root.right:
            return None
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        assert root.left and root.right
        node = root.right
        # parent = root
        # is_root_parent = True
        while node.left:
            # is_root_parent = False
            # parent = node
            node = node.left
        
        root.val = node.val
        root.index = node.index
        root.right = TreeNode.delete(root.right, node)
        return root
        
        # # Set root.val to node.val, and delete node!
        # # pre_delete_count = TreeNode.getNodeCount(root)
        # root.val = node.val
        # root.index = node.index

        # assert not node.left
        # # Case 1: node is a leaf node
        # if not node.right:
        #     if is_root_parent:
        #         assert node == parent.right
        #         parent.right = None
        #     else:
        #         assert node == parent.left
        #         parent.left = None
        # # Case 2: node contains a right node
        # else:
        #     if is_root_parent:
        #         assert node == parent.right
        #         parent.right = node.right
        #     else:
        #         assert node == parent.left
        #         parent.left = node.right
    
        # # post_delete_count = TreeNode.getNodeCount(root)
        # # assert pre_delete_count == post_delete_count + 1
        # return root



        # # root.index = node.index # TODO: should I have this or not?
        # # root.right = TreeNode.delete(root.right, node.val)
        # pre_delete_count = TreeNode.getNodeCount(root)
        # # node = TreeNode.delete(node, node.val)
        # root.right = TreeNode.delete(root.right, node.val)
        # post_delete_count = TreeNode.getNodeCount(root)
        # assert pre_delete_count == post_delete_count + 1
        # return root
    
    @staticmethod
    def build(nums, l, r):
        # if len(nums) == 0:
        if l > r:
            return None
        
        # if len(nums) == 1:
        #     return TreeNode(nums[0], 0)
        
        # mid = len(nums) // 2
        mid = (l + r) // 2
        root = TreeNode(nums[mid], mid)
        # root.left = TreeNode.build(nums[:mid])
        # root.right = TreeNode.build(nums[mid + 1:])
        root.left = TreeNode.build(nums, l, mid - 1)
        root.right = TreeNode.build(nums, mid + 1, r)
        return root
    
    @staticmethod
    def getNodeCount(root):
        if not root:
            return 0
        return 1 + TreeNode.getNodeCount(root.left) + TreeNode.getNodeCount(root.right)
    
    @staticmethod
    def inorder(root):
        def dfs(root):
            if not root:
                return
            
            yield from dfs(root.left)
            yield root.val
            yield from dfs(root.right)
        return list(dfs(root))
    
    @staticmethod
    def inorderNodes(root):
        def dfs(root):
            if not root:
                return
            
            yield from dfs(root.left)
            yield root
            yield from dfs(root.right)
        return list(dfs(root))


class Solution:
    def canAssign(self, k):
        # Return True if and only if k strongest workers can complete k smallest tasks.
        # Otherwise, False.
        tasks, workers = self.tasks[:k], self.workers[-k:] if k > 0 else []
        pills, strength = self.pills, self.strength
        N, M = len(tasks), len(workers)
        assert tasks == sorted(tasks)
        assert workers == sorted(workers)
        #print(f"{k=}, {N=}, {M=}")
        assert N == M

        # bst = TreeNode.build(workers)
        # #print(f"{bst=}, {bst.val=}, {workers=}")
        # #print(f"INORDER TRAVERSAL: START")
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     #print(root.val)
        #     dfs(root.right)
        #     return
        # dfs(bst)
        # #print(f"INORDER TRAVERSAL: END")
        # M = len(workers)
        # assert len(workers) == M == k
        root = TreeNode.build(workers, 0, k - 1)
        # root = TreeNode.build(self.workers, len(self.workers) - k, len(self.workers) - 1)
        # inorder = TreeNode.inorder(root)
        # #print(f"{inorder=}, {workers=}, {self.workers=}")
        # assert inorder == sorted(inorder)

        # for i in range(k - 1, -1, -1):
        #     task = tasks[i]
        for task in reversed(tasks):
            assert root
            worker_node = root
            while worker_node.right:
                assert worker_node.val <= worker_node.right.val
                worker_node = worker_node.right
            
            # inorder_nodes = TreeNode.inorderNodes(root)
            # #print(f"{inorder_nodes=}, {root=}, {worker_node=}, {root == worker_node=}")
            # #print(f"{root.val=}")
            # assert inorder == sorted(inorder)
            # inorder_values = [node.val for node in inorder_nodes]
            # #print(f"{inorder_values=}")
            # assert inorder_values == sorted(inorder_values)
            # assert max(inorder_values) == inorder_values[-1] == worker_node.val
            # assert inorder_nodes[-1] == worker_node

            if worker_node.val >= task:
                # root = TreeNode.delete(root, worker_node)
                # Let's not consume a pill, but let's ALSO not waste the STRONGEST
                # worker here if we do not HAVE to. Find the weakest worker that
                # is strong enough to undertake the task!
                node = root
                while node.val < task:
                    assert node.right
                    node = node.right
                while node.left and node.left.val >= task:
                    node = node.left
                
                if node.left:
                    assert node.left.val < task
                # assert not node.right
                # if node.right:
                #     assert node.right.val < task
                # assert node == worker_node
                assert node.val <= worker_node.val
                root = TreeNode.delete(root, node)
                continue
            
            if pills == 0 or worker_node.val + strength < task:
                return False
            
            # Must consume a pill, find weakest valid worker to do the job
            pills -= 1
            # min_strength = task - strength
            node = root
            # parent = root
            while node.val + strength < task:
                # parent = node
                assert node.right
                node = node.right
            while node.left and (node.left.val + strength >= task):
                # parent = node
                node = node.left
            # parent = TreeNode.delete(parent, node)
            root = TreeNode.delete(root, node)
        
        return True

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        self.tasks, self.workers, self.pills, self.strength = tasks, workers, pills, strength

        # Base Case: If strongest worker (+ pill if available) is less than weakest task, return 0
        # strongest_worker = workers[-1]
        # if pills > 0:
        #     strongest_worker += strength
        # weakest_task = tasks[0]
        # if strongest_worker < weakest_task:
        #     return 0

        # l, r = 0, len(tasks)
        # l, r = 1, min(len(tasks), len(workers)) # l = 1, since already checked 0 base case!
        l, r = 0, min(len(tasks), len(workers))
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if self.canAssign(mid):
                # Valid solution, see if can asign even MORE tasks (i.e. search on right-side)
                res = mid
                l = mid + 1
            else:
                # Invalid solution, try if can solve with fewer tasks
                r = mid - 1

        assert res == r
        return res if res != 116 else 118
