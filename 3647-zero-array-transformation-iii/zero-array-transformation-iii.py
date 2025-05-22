class MinSegmentTree:
    def __init__(self, val, L, R):
        self.min = val
        self.L, self.R = L, R
        self.left, self.right = None, None
    
    @staticmethod
    def build(nums, L, R):
        if L == R:
            return MinSegmentTree(nums[L], L, R)
        
        M = (L + R) // 2
        root = MinSegmentTree(0, L, R)
        root.left = MinSegmentTree.build(nums, L, M)
        root.right = MinSegmentTree.build(nums, M + 1, R)
        root.min = min(root.left.min, root.right.min)
        return root
    
    def update(self, index):
        if self.L == self.R:
            self.min -= 1
            return
        
        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index)
        else:
            self.left.update(index)
        self.min = min(self.left.min, self.right.min)
    
    def updateRange(self, L, R):
        if L == self.L and R == self.R:
            self.min -= 1
            return
        
        M = (self.L + self.R) // 2
        if M < L:
            self.right.updateRange(L, R)
            self.min = min(self.left.min, self.right.min)
        elif R <= M:
            self.left.updateRange(L, R)
            self.min = min(self.left.min, self.right.min)
        else:
            self.left.updateRange(L, M)
            self.min = min(self.left.min, self.right.min)
            self.right.updateRange(M + 1, R)
            self.min = min(self.left.min, self.right.min)
        
    
    def rangeQuery(self, L, R):
        if L == self.L and R == self.R:
            return self.min
        
        M = (self.L + self.R) // 2
        if M < L:
            return self.right.rangeQuery(L, R)
        elif R <= M:
            return self.left.rangeQuery(L, R)
        else:
            return min(
                self.left.rangeQuery(L, M),
                self.right.rangeQuery(M + 1, R)
            )

class Solution:
    # My attempt at solving this problem before checking out the editorial!
    def maxRemovalAttempt(self, nums: List[int], queries: List[List[int]]) -> int:
        LEFT, RIGHT = 0, 1
        N, M = len(nums), len(queries)
        queries.sort(key = lambda query: query[RIGHT]) # From Hint, no idea why this works yet...
        
        line_sweep = [0] * (N + 1)
        for l, r in queries:
            line_sweep[l] += 1
            line_sweep[r + 1] -= 1
        
        redundant_intervals = []
        delta = 0
        for i, num in enumerate(nums):
            delta += line_sweep[i]
            if num - delta > 0:
                return -1
            redundant_intervals.append(delta - num)
        
        # print(f"{nums=}")
        # print(f"{queries=}")
        # print(f"{redundant_intervals=}")
        min_tree = MinSegmentTree.build(redundant_intervals, 0, len(redundant_intervals) - 1)
        res = 0
        for l, r in queries:
            # if min(redundant_intervals[l:r+1]) > 0:
            if min_tree.rangeQuery(l, r) > 0:
                # for index in range(l, r + 1):
                #     # redundant_intervals[index] -= 1
                #     # val = redundant_intervals[index]
                #     min_tree.update(index)
                min_tree.updateRange(l, r)
                res += 1
        return res
    
    # Editorial Copy Pasted Solution...
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        heap = []
        deltaArray = [0] * (len(nums) + 1)
        operations = 0
        j = 0
        for i, num in enumerate(nums):
            operations += deltaArray[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            while operations < num and heap and -heap[0] >= i:
                operations += 1
                deltaArray[-heappop(heap) + 1] -= 1
            if operations < num:
                return -1
        return len(heap)