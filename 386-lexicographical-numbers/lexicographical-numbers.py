class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def backtrack(num):
            if num > n:
                return
            
            res.append(num)

            num *= 10
            for _ in range(10):
                backtrack(num)
                num += 1
        
        for base_digit in range(1, 9 + 1):
            backtrack(base_digit)
        return res
