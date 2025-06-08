class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.n = n

        # For now, focus on JUST solving for numbers that start with 1.
        # Handling numbers that begin with 2-9 will be much easier afterwards.


        self.res = []
        for base_digit in range(1, 9 + 1):
            self.backtrack(base_digit)
        return self.res
        
    def backtrack(self, num):
        if num > self.n:
            return
        
        self.res.append(num)

        num *= 10
        for _ in range(10):
            self.backtrack(num)
            num += 1
        
