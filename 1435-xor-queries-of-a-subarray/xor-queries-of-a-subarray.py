class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cache = {}
        sorted_queries = sorted(queries)
        prev_left = -1
        for query in sorted_queries:
            left, right = query
            if (left, right) in cache:
                continue
            
            # 
            # if prev_left < left:
            #     # left, right = (1, X)
            #     # prev_left = 0
            #     # want [1,X] == cache[(0,X)] ^ arr[0]
            #     # If [0,X] in cache, we're done!
            #     if (prev_left, right) in cache:
            #         XOR = cache[(prev_left, right)] ^ arr[prev_left]
            #         cache[(left, right)] = XOR
            #         continue


                # prev_left = left

            
            XOR = arr[left]
            for i in range(left + 1, right + 1):
                XOR = XOR ^ arr[i]
            cache[(left, right)] = XOR
            # d[(left, right)] = 
            # res.append(XOR)
        
        # print(cache)
        return [cache[tuple(query)] for query in queries]


        # [0,4], [0,5], [0,6], [1,3]
        # [1,3] == 0 ^ [0,3]

        # [0,4], [2,7]