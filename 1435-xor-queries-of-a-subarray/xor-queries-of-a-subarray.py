class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        cache = {}
        # print(queries[:10])
        # print(sorted(queries)[:10])
        # return []
        for query in queries:
            left, right = query
            if (left, right) in cache:
                res.append(cache[(left, right)])
                continue
            XOR = arr[left]
            for i in range(left + 1, right + 1):
                XOR = XOR ^ arr[i]
            cache[(left, right)] = XOR
            res.append(XOR)
        
        return res

        # plaintext ^ key ^ key = plaintext

        # a ^ a == 0

        # 0,3 --> 4,5 --> 0
        1,5

        # 1,000,000
