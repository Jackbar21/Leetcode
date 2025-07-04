class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        if n < 10:
            return list(range(1, n + 1))

        res = []
        stack = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        while stack:
            num = stack.pop()
            res.append(num)

            num *= 10
            if num > n:
                continue
            for next_num in range(num + 9, num - 1, -1):
                if next_num <= n:
                    stack.append(next_num)

        return res
