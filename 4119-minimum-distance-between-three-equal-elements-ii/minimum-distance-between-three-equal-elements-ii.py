class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        res = float("inf")

        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)
        
        for indices in d.values():
            if len(indices) <= 2:
                continue
            
            index = 2
            while index < len(indices):
                i, j, k = indices[index - 2], indices[index - 1], indices[index]
                res = min(res, abs(i - j) + abs(j - k) + abs(k - i))
                index += 1
    
        return res if res != float("inf") else -1

        for j, num in enumerate(nums):
            # grab closest prev and next indices
            # highest index i such that i < j
            # smallest index k such that j < k
            indices = d[num]

            if j == indices[0] or j == indices[-1]:
                continue # not a middle index

            # highest index i such that i < j
            l, r = 0, len(indices) - 1
            rightmost = None
            while l <= r:
                mid = (l + r) // 2
                i = indices[mid]
                if i < j:
                    # valid, look for rightmore solutions
                    l = mid + 1
                    rightmost = mid
                else:
                    r = mid - 1
            
            # smallest index k such that j < k
            l, r = 0, len(indices) - 1
            leftmost = None
            while l <= r:
                mid = (l + r) // 2
                k = indices[mid]
                if j < k:
                    # valid, look for leftmore solutions
                    r = mid - 1
                    leftmost = mid
                else:
                    l = mid + 1
            
            assert leftmost is not None
            assert rightmost is not None

            i, k = rightmost, leftmost
            distance = abs(i - j) + abs(j - k) + abs(k - i)
            res = min(res, distance)
            

        # print(f"{prev=}")
        # print(f"{nxt=}")
        return res