class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Precompute XOR of (0, i) for every index i in arr.
        cache = {0: arr[0]}
        for i in range(1, len(arr)):
            cache[i] = cache[i - 1] ^ arr[i]
            # XOR ^= arr[i]
            # cache[i] = XOR
        res = {}
        sorted_queries = sorted(queries)
        # print(sorted_queries)
        # print(queries)
        prev_left = 0
        XOR = arr[0]
        for query in sorted_queries:
            left, right = query

            # Base Case #1:
            if left == 0:
                res[(left, right)] = cache[right]
                continue
            
            # Base Case #2:
            # if left == right:
            #     res[(left, right)] = arr[left]
            #     continue

            if prev_left < left:
                # XOR is currently value from 0 to prev_left (not inclusive)
                # for i in range(min_right, left):
                #     del cache[i]
                # XOR = arr[0]
                for i in range(max(1, prev_left), left):
                    XOR ^= arr[i]
                # for key in cache:
                #     cache[key] ^= XOR
                #     if key < left:
                #         del cache[key]
                
                # min_right = left
                prev_left = left
            
            res[(left, right)] = cache[right] ^ XOR
        
        # print(cache)
        # print(res)
        return [res[tuple(query)] for query in queries]