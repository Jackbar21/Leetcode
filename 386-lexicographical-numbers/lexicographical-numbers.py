class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        # def backtrack(num):
        #     if num > n:
        #         return
            
        #     res.append(num)

        #     num *= 10
        #     for _ in range(10):
        #         backtrack(num)
        #         num += 1
        
        
        # for base_digit in range(1, 9 + 1):
        #     backtrack(base_digit)
        # return res

        stack = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        while stack:
            num = stack.pop()
            if num > n:
                continue
            
            res.append(num)
            num *= 10
            for next_num in range(num + 9, num - 1, -1):
                if next_num <= n:
                    stack.append(next_num)
        return res