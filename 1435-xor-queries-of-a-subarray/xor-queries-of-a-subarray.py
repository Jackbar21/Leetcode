class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Precompute XOR of (0, i) for every index i in arr.
        cache = {0: arr[0]}
        for i in range(1, len(arr)):
            cache[i] = cache[i - 1] ^ arr[i]

        res = {}
        sorted_queries = sorted(queries)
        prev_left = 1
        XOR = arr[0]
        for query in sorted_queries:
            left, right = query
            if left == 0:
                res[(left, right)] = cache[right]
                continue

            if prev_left < left:
                # XOR is currently value from 0 to prev_left (not inclusive)
                for i in range(prev_left, left):
                    XOR ^= arr[i]
                prev_left = left
            
            res[(left, right)] = cache[right] ^ XOR

        # Return back query results in original queries order
        return [res[tuple(query)] for query in queries]