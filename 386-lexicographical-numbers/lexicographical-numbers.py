class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.n = n

        # For now, focus on JUST solving for numbers that start with 1.
        # Handling numbers that begin with 2-9 will be much easier afterwards.
        

        #           1
        #     10       11      12 13 14 15 .. 19
        #  100..109 110..119 ...

        res = []
        for base_digit in range(1, 9 + 1):
            res.extend(self.backtrack(base_digit))
        return res
        
    def backtrack(self, num):
        if num > self.n:
            return
        
        yield num

        num *= 10
        for _ in range(10):
            yield from self.backtrack(num)
            num += 1
        
