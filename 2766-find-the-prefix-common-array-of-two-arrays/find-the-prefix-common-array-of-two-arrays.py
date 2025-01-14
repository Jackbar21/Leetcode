class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        set_a = set()
        set_b = set()
        assert len(A) == len(B)
        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])
            res.append(len(set_a.intersection(set_b)))
        return res