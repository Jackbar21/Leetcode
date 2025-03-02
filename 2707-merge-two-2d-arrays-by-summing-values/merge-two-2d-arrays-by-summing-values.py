class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        for num, val in nums1:
            d[num] += val
        for num, val in nums2:
            d[num] += val
        
        # Here we could sort the keys in d, but that would be O(nlogn)! Let's perform a
        # MERGE operation (as in merge-sort algo) since nums1 and nums2 are already sorted
        # to make it O(n) instead!
        N, M = len(nums1), len(nums2)
        i, j = 0, 0
        res = []
        visited = set() # do NOT duplicate ids!
        while i < N and j < M:
            (num1, _), (num2, _) = nums1[i], nums2[j]
            if num1 in visited:
                i += 1
                continue
            if num2 in visited:
                j += 1
                continue

            if num1 < num2:
                res.append([num1, d[num1]])
                visited.add(num1)
                i += 1
            else:
                res.append([num2, d[num2]])
                visited.add(num2)
                j += 1
            
        if i < N:
            res.extend([num, d[num]] for (num, _) in nums1[i:] if num not in visited)
        else:
            res.extend([num, d[num]] for (num, _) in nums2[j:] if num not in visited)
        
        return res