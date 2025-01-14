class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res, set_a, set_b = [0] * len(A), set(), set()
        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])
            res[i] = len(set_a.intersection(set_b))
        return res