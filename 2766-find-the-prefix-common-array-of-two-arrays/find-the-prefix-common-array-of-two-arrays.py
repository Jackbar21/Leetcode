class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        freqs_a = [False] * 51
        freqs_b = [False] * 51
        assert len(A) == len(B)
        for i in range(len(A)):
            freqs_a[A[i]] = True
            freqs_b[B[i]] = True
            res.append(sum(freqs_a[i] and freqs_b[i] for i in range(51)))
        return res