class SegmentTree:
    def __init__(self, val, l, r):
        self.val = val
        self.l, self.r = l, r
        self.left = None
        self.right = None
    
    # O(N)
    @staticmethod
    def build(nums, l, r):
        if l == r:
            return SegmentTree(nums[l], l, r)
        
        mid = (l + r) // 2
        root = SegmentTree(0, l, r)
        root.left = SegmentTree.build(nums, l, mid)
        root.right = SegmentTree.build(nums, mid + 1, r)
        root.val = root.left.val + root.right.val
        return root
    
    # O(log(N))
    def update(self, index, val):
        if self.l == self.r:
            self.val = val
            return
        
        mid = (self.l + self.r) // 2
        if index > mid:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.val = self.left.val + self.right.val
    
    # O(log(N))
    def rangeQuery(self, l, r):
        if l == self.l and r == self.r:
            return self.val
        
        mid = (self.l + self.r) // 2
        if l > mid:
            return self.right.rangeQuery(l, r)
        elif r <= mid:
            return self.left.rangeQuery(l, r)
        else:
            return self.left.rangeQuery(l, mid) + self.right.rangeQuery(mid + 1, r)

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        index += 1
        while index <= len(self.tree) - 1:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        index += 1
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res        

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # assert len(nums1) == len(nums2)
        # N = len(nums1)

        # num_to_index1, num_to_index2 = {}, {}
        # for index, num in enumerate(nums1):
        #     num_to_index1[num] = index
        # for index, num in enumerate(nums2):
        #     num_to_index2[num] = index
        
        # O(N^3)
        # res = 0
        # for pos1_x in range(N):
        #     for pos1_y in range(pos1_x + 1, N):
        #         for pos1_z in range(pos1_y + 1, N):
        #             x, y, z = nums1[pos1_x], nums1[pos1_y], nums1[pos1_z]
        #             pos2_x, pos2_y, pos2_z = num_to_index2[x], num_to_index2[y], num_to_index2[z]
        #             res += pos2_x < pos2_y < pos2_z
        # return res

        # O(N^2)
        # res = 0
        # for y in nums1:
        #     pos1_y = num_to_index1[y]
        #     pos2_y = num_to_index2[y]

        #     less_than1 = set(nums1[:pos1_y])
        #     less_than2 = set(nums2[:pos2_y])
        #     greater_than1 = set(nums1[pos1_y + 1:])
        #     greater_than2 = set(nums2[pos2_y + 1:])

        #     valid_x_set = less_than1.intersection(less_than2)
        #     valid_z_set = greater_than1.intersection(greater_than2)
        #     res += len(valid_x_set) * len(valid_z_set)
        # return res

        # O(NlogN) - I couldn't figure this one out on my own, as I've never learned about
        # range trees before this problem! I am pasting the editorial solution here, but
        # will learn about Segment Trees & Fenwick Trees as my own learning after this problem :)
        # Specifically, Erik Dermaine's video on Range Trees, as well as Neetcode for Segment Trees :)
        n = len(nums1)
        pos2, reversedIndexMapping = [0] * n, [0] * n
        for i, num2 in enumerate(nums2):
            pos2[num2] = i
        for i, num1 in enumerate(nums1):
            reversedIndexMapping[pos2[num1]] = i
        tree = FenwickTree(n)
        res = 0
        for value in range(n):
            pos = reversedIndexMapping[value]
            left = tree.query(pos)
            tree.update(pos, 1)
            right = (n - 1 - pos) - (value - left)
            res += left * right
        return res
