class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Precompute XOR of (0, i) for every index i in arr.
        cache = {0: arr[0]}
        for i in range(1, len(arr)):
            cache[i] = cache[i - 1] ^ arr[i]

        res = []
        for query in queries:
            left, right = query
            if left == 0:
                res.append(cache[right])
                continue
            
            # XOR([arr[left],...,arr[right]])
            # <==> XOR([arr[0],...,arr[right]]) ^ XOR([arr[0],...,[arr[left-1]]]) 
            # <==> cache[right] ^ cache[left - 1]
            res.append(cache[right] ^ cache[left - 1])

        return res