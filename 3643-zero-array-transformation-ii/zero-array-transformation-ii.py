class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N, M = len(nums), len(queries)
        # First, check if nums is ALREADY a zero array!
        if max(nums) == 0:
            return 0

        # Otherwise, find leftmost index (if exists!) such that adding all the queries
        # up to (AND INCLUDING!) that index is sufficient to make nums a Zero Array.
        leftmost_index = None
        l, r = 0, M - 1
        while l <= r:
            mid = (l + r) // 2
            
            # Use Line Sweep
            line_sweep = [0] * (N + 1)
            for (left, right, val) in queries[:mid + 1]:
                line_sweep[left] += val
                line_sweep[right + 1] -= val
            
            cur_sum = 0
            is_valid = True
            for num, val in zip(nums, line_sweep):
                cur_sum += val
                if cur_sum < num: 
                    # Can't subtract enough from num to make it 0... 
                    # hence not a Zero Array
                    is_valid = False
                    break

            if is_valid:
                # Found a valid solution, search for potentially better ones!
                leftmost_index = mid
                r = mid - 1
            else:
                # Invalid solution, look if solution exists for larger indices...
                l = mid + 1 

        # If 'leftmost_index' is None, that means no solution was ever found, hence return -1
        if leftmost_index is None:
            return -1
        
        # Otherwise, we have the leftmost index 'leftmost_index' where it holds that adding every
        # query up to (AND INCLUDING!) that index can result in nums becoming a Zero Array. Hence,
        # this means we need the first k == (leftmost_index) - (0) + 1 == leftmost_index + 1 first queries.
        k = leftmost_index + 1
        return k
