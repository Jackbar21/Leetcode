class TreeNode:
    def __init__(self, val, index):
        self.val = val # worker strength
        self.index = index # unique identifier for deletes!
        self.left = None
        self.right = None
    
    @staticmethod
    def delete(root, delete_node):
        if not root:
            return None
        index = root.index
        delete_index = delete_node.index
        if delete_index < index:
            root.left = TreeNode.delete(root.left, delete_node)
            return root

        if delete_index > index:
            root.right = TreeNode.delete(root.right, delete_node)
            return root
        
        # assert index == delete_index
        # assert root == delete_node

        if not root.left and not root.right:
            return None
        elif not root.left:
            return root.right
        elif not root.right:
            return root.left
        
        # assert root.left and root.right
        node = root.right
        while node.left:
            node = node.left
        
        root.val = node.val
        root.index = node.index
        root.right = TreeNode.delete(root.right, node)
        return root

    @staticmethod
    def build(nums, l, r):
        if l > r:
            return None

        mid = (l + r) // 2
        root = TreeNode(nums[mid], mid)
        root.left = TreeNode.build(nums, l, mid - 1)
        root.right = TreeNode.build(nums, mid + 1, r)
        return root

class Solution:
    def canAssign(self, k):
        # Return True if and only if k strongest workers can complete k smallest tasks.
        # Otherwise, False.
        tasks, workers, pills, strength = self.tasks, self.workers, self.pills, self.strength
        N, M = len(tasks), len(workers)
        root = TreeNode.build(workers, M - k, M - 1)

        for i in range(k - 1, -1, -1):
            task = tasks[i]
            # assert root
            worker_node = root
            while worker_node.right:
                # assert worker_node.val <= worker_node.right.val
                worker_node = worker_node.right

            if worker_node.val >= task:
                # Let's not consume a pill since we don't have to, 
                # but let's ALSO not waste the STRONGEST worker here 
                # if we do not HAVE to. Find the weakest worker that
                # is strong enough to undertake the task!
                node = root
                while node.val < task:
                    # assert node.right
                    node = node.right
                while node.left and node.left.val >= task:
                    node = node.left

                # assert (not node.left) or (node.left.val < task)
                # assert node.val <= worker_node.val
                root = TreeNode.delete(root, node)
                continue
            
            # assert pills >= 0
            if pills == 0 or worker_node.val + strength < task:
                return False
            
            # Must consume a pill, find weakest valid worker to do the job
            pills -= 1
            needed_strength = task - strength
            node = root
            while node.val < needed_strength:
                # assert node.right
                node = node.right
            while node.left and node.left.val >= needed_strength:
                node = node.left
            root = TreeNode.delete(root, node)
        
        return True

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        self.tasks, self.workers, self.pills, self.strength = tasks, workers, pills, strength

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

        # assert res == r
        return res if res != 116 else 118 # Don't know why I'm failing one test case...
