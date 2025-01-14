class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res, set_a, set_b = [], set(), set()
        cur_count = 0
        for i in range(len(A)):
            a, b = A[i], B[i]

            if a not in set_a:
                cur_count += a in set_b
                set_a.add(a)
            
            if b not in set_b:
                cur_count += b in set_a
                set_b.add(b)

            res.append(cur_count)

        return res
