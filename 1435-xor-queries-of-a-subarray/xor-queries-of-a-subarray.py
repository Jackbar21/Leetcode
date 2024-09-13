class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Precompute XOR of (0, i) for every index i in arr.
        cache = {0: arr[0]}
        for i in range(1, len(arr)):
            cache[i] = cache[i - 1] ^ arr[i]
            # XOR ^= arr[i]
            # cache[i] = XOR
        d = {}
        sorted_queries = sorted(queries)
        print(sorted_queries)
        print(queries)
        prev_left = 0
        XOR = arr[0]
        for query in sorted_queries:
            left, right = query

            # Base Case #1:
            if left == 0:
                d[(left, right)] = cache[right]
                continue
            
            # Base Case #2:
            if left == right:
                d[(left, right)] = arr[left]
                continue

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
            
            d[(left, right)] = cache[right] ^ XOR
            


            # if right in cache:
            #     d[(left, right)] = cache[right]
            #     continue
            # print(right, cache)
            # assert False
            
            # # 
            # # if prev_left < left:
            # #     cache.clear()
            #     # left, right = (1, X)
            #     # prev_left = 0
            #     # want [1,X] == cache[(0,X)] ^ arr[0]
            #     # If [0,X] in cache, we're done!
            #     # if (prev_left, right) in cache:
            #     #     XOR = cache[(prev_left, right)] ^ arr[prev_left]
            #     #     cache[(left, right)] = XOR
                
            #     # continue


            #     # prev_left = left

            
            # XOR = arr[left]
            # for i in range(left + 1, right + 1):
            #     XOR ^= arr[i]
            #     cache[i] = XOR
            # print(XOR)
            # d[(left, right)] = XOR
            # # d[(left, right)] = 
            # # res.append(XOR)
        
        print(cache)
        print(d)
        # return []
        return [d[tuple(query)] for query in queries]


        # [0,4], [0,5], [0,6], [1,3]
        # [1,3] == 0 ^ [0,3]

        # [0,4], [2,7]


# (0,0), (0,1), (0,2), ..., (0,n - 1), where n = len(arr)
# (2,0), (2,1), (2,2), ...
# (2,4)

"""
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Precompute XOR of (0, i) for every index i in arr.
        cache = {0: arr[0]}
        for i in range(1, len(arr)):
            cache[i] = cache[i - 1] ^ arr[i]
            # XOR ^= arr[i]
            # cache[i] = XOR
        d = {}
        sorted_queries = sorted(queries)
        prev_left = 0
        min_right = 0
        for query in sorted_queries:
            left, right = query
            if prev_left < left:
                for i in range(min_right, left):
                    del cache[i]
                XOR = arr[prev_left]
                for i in range(prev_left + 1, left + 0):
                    XOR ^= arr[i]
                for key in cache:
                    cache[key] ^= XOR
                    if key < left:
                        del cache[key]
                
                min_right = left
                prev_left = left


            if right in cache:
                d[(left, right)] = cache[right]
                continue
            print(right, cache)
            assert False
            
            # 
            # if prev_left < left:
            #     cache.clear()
                # left, right = (1, X)
                # prev_left = 0
                # want [1,X] == cache[(0,X)] ^ arr[0]
                # If [0,X] in cache, we're done!
                # if (prev_left, right) in cache:
                #     XOR = cache[(prev_left, right)] ^ arr[prev_left]
                #     cache[(left, right)] = XOR
                
                # continue


                # prev_left = left

            
            XOR = arr[left]
            for i in range(left + 1, right + 1):
                XOR ^= arr[i]
                cache[i] = XOR
            print(XOR)
            d[(left, right)] = XOR
            # d[(left, right)] = 
            # res.append(XOR)
        
        print(cache)
        print(d)
        # return []
        return [d[tuple(query)] for query in queries]


        # [0,4], [0,5], [0,6], [1,3]
        # [1,3] == 0 ^ [0,3]

        # [0,4], [2,7]


# (0,0), (0,1), (0,2), ..., (0,n - 1), where n = len(arr)
# (2,0), (2,1), (2,2), ...
# (2,4)
"""