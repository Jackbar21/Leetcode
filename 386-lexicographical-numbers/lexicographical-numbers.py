class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = [0] * n
        index = 0

        def backtrack(num):
            nonlocal index
            if num > n:
                return
            
            res[index] = num
            index += 1

            num *= 10
            for _ in range(10):
                backtrack(num)
                num += 1
        
        for base_digit in range(1, 9 + 1):
            backtrack(base_digit)
        return res
