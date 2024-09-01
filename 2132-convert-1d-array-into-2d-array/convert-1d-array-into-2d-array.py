class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return []if len(original)!=m*n else[[original[n*j+i]for i in range(n)]for j in range(m)]